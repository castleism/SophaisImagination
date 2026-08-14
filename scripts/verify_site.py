#!/usr/bin/env python3
"""Verify and optionally assemble the public GitHub Pages artifact.

The script deliberately uses only the Python standard library so the same
checks run on the owner's Windows machine and GitHub's Ubuntu runner.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import struct
import sys
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree


REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = REPO_ROOT / ".pages-manifest"

ROOT_PUBLIC_NAMES = {".nojekyll", "CNAME", "robots.txt", "sitemap.xml"}
ROOT_PUBLIC_SUFFIXES = {
    ".avif",
    ".css",
    ".gif",
    ".html",
    ".ico",
    ".jpeg",
    ".jpg",
    ".js",
    ".json",
    ".png",
    ".svg",
    ".txt",
    ".webmanifest",
    ".webp",
    ".woff",
    ".woff2",
    ".xml",
}
TEXT_SUFFIXES = {".html", ".css", ".js", ".json", ".xml", ".txt", ".svg", ".webmanifest"}
ALLOWED_ASSET_SUFFIXES = {
    ".avif",
    ".css",
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".js",
    ".json",
    ".png",
    ".svg",
    ".txt",
    ".webmanifest",
    ".webp",
    ".woff",
    ".woff2",
}
SENSITIVE_PATH_PARTS = {
    "_to_delete",
    "backup",
    "backups",
    "credential",
    "credentials",
    "original",
    "originals",
    "private",
    "prompt",
    "prompts",
    "reference",
    "references",
    "rejected",
    "secret",
    "secrets",
    "source",
    "sources",
    "token",
    "tokens",
}
APPROVED_PUBLIC_EMAILS: set[str] = set()

EMAIL_RE = re.compile(r"(?i)(?<![\w.+-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![\w.-])")
WINDOWS_PATH_RE = re.compile(r"(?i)(?:\\\\\?\\)?\b[A-Z]:[\\/]")
UNIX_PRIVATE_PATH_RE = re.compile(r"(?i)(?:^|[\s\"'=])/(?:Users|home)/[^/\s\"']+/")
ROOT_PRIVATE_PATH_RE = re.compile(r"(?i)(?:^|[\s\"'=])/root/")
ADULT_LANE_RE = re.compile(
    r"(?i)\b(?:onlyfans|nsfw|18\+|adult[-\s]?(?:content|lane|platform|subscription|brand)|explicit[-\s]content)\b"
)
GOOGLE_FONT_RE = re.compile(r"(?i)fonts\.(?:googleapis|gstatic)\.com")
CSS_URL_RE = re.compile(r"url\(\s*(['\"]?)([^'\")]+)\1\s*\)", re.IGNORECASE)


class PublicHTMLParser(HTMLParser):
    """Collect structural, reference, and deliberate truth-state markers."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.h1_count = 0
        self.main_count = 0
        self.ids: set[str] = set()
        self.references: list[tuple[str, str]] = []
        self.blank_targets_without_noopener: list[str] = []
        self.noindex = False
        self.verified_release_links: list[str] = []
        self.verified_instagram_links: list[str] = []
        self.verified_result_markers = 0
        self._json_ld_depth = 0
        self._json_ld_chunks: list[str] = []
        self.json_ld_documents: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._handle_tag(tag, attrs)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._handle_tag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script" and self._json_ld_depth:
            self.json_ld_documents.append("".join(self._json_ld_chunks).strip())
            self._json_ld_depth = 0
            self._json_ld_chunks = []

    def handle_data(self, data: str) -> None:
        if self._json_ld_depth:
            self._json_ld_chunks.append(data)

    def _handle_tag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attr = {name.lower(): value or "" for name, value in attrs}

        if tag == "h1":
            self.h1_count += 1
        elif tag == "main":
            self.main_count += 1

        if attr.get("id"):
            self.ids.add(attr["id"])

        if tag == "meta" and attr.get("name", "").lower() == "robots":
            if "noindex" in attr.get("content", "").lower():
                self.noindex = True

        if tag == "script" and attr.get("type", "").lower() == "application/ld+json":
            self._json_ld_depth = 1
            self._json_ld_chunks = []

        reference_attrs = {
            "a": ("href",),
            "audio": ("src",),
            "form": ("action",),
            "iframe": ("src",),
            "img": ("src", "srcset"),
            "link": ("href",),
            "script": ("src",),
            "source": ("src", "srcset"),
            "track": ("src",),
            "video": ("src", "poster"),
        }
        for name in reference_attrs.get(tag, ()):
            if attr.get(name):
                values = _split_srcset(attr[name]) if name == "srcset" else [attr[name]]
                self.references.extend((name, value) for value in values)

        if tag == "a" and attr.get("target", "").lower() == "_blank":
            rel = {token.lower() for token in attr.get("rel", "").split()}
            if "noopener" not in rel:
                self.blank_targets_without_noopener.append(attr.get("href", "<missing href>"))

        if attr.get("data-verifiable-release", "").lower() == "true":
            href = attr.get("href", "")
            if tag == "a" and _is_external_https(href):
                self.verified_release_links.append(href)

        if attr.get("data-verified-account", "").lower() == "true":
            href = attr.get("href", "")
            if tag == "a" and _is_instagram_url(href):
                self.verified_instagram_links.append(href)

        if attr.get("data-verified-result", "").lower() == "true":
            self.verified_result_markers += 1


def _split_srcset(value: str) -> list[str]:
    candidates: list[str] = []
    for item in value.split(","):
        candidate = item.strip().split()
        if candidate:
            candidates.append(candidate[0])
    return candidates


def _is_external_https(value: str) -> bool:
    parsed = urlsplit(value)
    return parsed.scheme.lower() == "https" and bool(parsed.netloc)


def _is_instagram_url(value: str) -> bool:
    parsed = urlsplit(value)
    host = parsed.netloc.lower().split(":", 1)[0]
    return parsed.scheme.lower() == "https" and host in {"instagram.com", "www.instagram.com"}


def _display(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path)


def _parse_manifest(errors: list[str]) -> tuple[list[PurePosixPath], set[str]]:
    entries: list[PurePosixPath] = []
    expanded: set[str] = set()

    if not MANIFEST_PATH.is_file():
        errors.append("Missing .pages-manifest.")
        return entries, expanded

    seen_entries: set[str] = set()
    for line_number, raw_line in enumerate(MANIFEST_PATH.read_text(encoding="utf-8").splitlines(), 1):
        value = raw_line.strip()
        if not value or value.startswith("#"):
            continue
        value = value.replace("\\", "/")
        is_directory = value.endswith("/")
        normalized_value = value.rstrip("/")
        posix = PurePosixPath(normalized_value)

        if not normalized_value or posix.is_absolute() or ".." in posix.parts or normalized_value == ".":
            errors.append(f".pages-manifest:{line_number}: unsafe path {raw_line!r}.")
            continue
        if any(character in value for character in "*?[]"):
            errors.append(f".pages-manifest:{line_number}: globs are not allowed ({value!r}).")
            continue

        entry_key = normalized_value + ("/" if is_directory else "")
        if entry_key in seen_entries:
            errors.append(f".pages-manifest:{line_number}: duplicate entry {entry_key!r}.")
            continue
        seen_entries.add(entry_key)
        entries.append(PurePosixPath(entry_key))

        source = REPO_ROOT.joinpath(*posix.parts)
        if source.is_symlink():
            errors.append(f"Manifest entry may not be a symlink: {entry_key}.")
            continue
        if is_directory:
            if not source.is_dir():
                errors.append(f"Manifest directory does not exist: {entry_key}.")
                continue
            for child in sorted(source.rglob("*")):
                if child.is_symlink():
                    errors.append(f"Public directory contains a symlink: {_display(child)}.")
                elif child.is_file():
                    expanded.add(child.relative_to(REPO_ROOT).as_posix())
        else:
            if not source.is_file():
                errors.append(f"Manifest file does not exist: {entry_key}.")
                continue
            expanded.add(normalized_value)

    if not entries:
        errors.append(".pages-manifest has no public entries.")
    return entries, expanded


def _check_manifest_completeness(expanded: set[str], errors: list[str]) -> None:
    public_candidates: set[str] = set()
    for path in REPO_ROOT.iterdir():
        if not path.is_file() or path.name == ".pages-manifest":
            continue
        if path.name in ROOT_PUBLIC_NAMES or path.suffix.lower() in ROOT_PUBLIC_SUFFIXES:
            public_candidates.add(path.name)

    missing = sorted(public_candidates - expanded)
    if missing:
        errors.append("Root public files missing from .pages-manifest: " + ", ".join(missing) + ".")

    required = {".nojekyll", "404.html", "CNAME", "index.html", "robots.txt", "sitemap.xml"}
    required_missing = sorted(required - expanded)
    if required_missing:
        errors.append("Required Pages files missing from the artifact: " + ", ".join(required_missing) + ".")


def _read_public_text(path: Path, errors: list[str]) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"Public text file is not valid UTF-8: {_display(path)}.")
    except OSError as exc:
        errors.append(f"Could not read {_display(path)}: {exc}.")
    return None


def _check_public_safety(relative: str, text: str, errors: list[str]) -> None:
    checks = (
        (GOOGLE_FONT_RE, "references a Google Fonts host; self-host fonts instead"),
        (WINDOWS_PATH_RE, "contains a Windows absolute path"),
        (UNIX_PRIVATE_PATH_RE, "contains a private Unix home path"),
        (ROOT_PRIVATE_PATH_RE, "contains a private root path"),
        (ADULT_LANE_RE, "contains a prohibited adult-lane term"),
    )
    for pattern, message in checks:
        match = pattern.search(text)
        if match:
            errors.append(f"{relative}: {message} ({match.group(0)!r}).")

    for match in EMAIL_RE.finditer(text):
        address = match.group(0).lower()
        if address not in APPROVED_PUBLIC_EMAILS:
            line_number = text.count("\n", 0, match.start()) + 1
            errors.append(
                f"{relative}:{line_number}: contains an unapproved public email address; it was not printed. "
                "Add only an explicitly owner-approved public alias to APPROVED_PUBLIC_EMAILS."
            )


def _check_repository_document_safety(errors: list[str]) -> None:
    """Protect documentation in the public Git repository, not only the Pages artifact."""
    candidates = [
        path
        for path in REPO_ROOT.iterdir()
        if path.is_file() and path.suffix.lower() == ".md"
    ]
    docs = REPO_ROOT / "docs"
    if docs.is_dir():
        candidates.extend(path for path in docs.rglob("*.md") if path.is_file())

    checks = (
        (WINDOWS_PATH_RE, "contains a Windows absolute path"),
        (UNIX_PRIVATE_PATH_RE, "contains a private Unix home path"),
        (ROOT_PRIVATE_PATH_RE, "contains a private root path"),
        (ADULT_LANE_RE, "contains a prohibited cross-lane term"),
    )
    for path in sorted(set(candidates)):
        relative = _display(path)
        text = _read_public_text(path, errors)
        if text is None:
            continue
        for pattern, message in checks:
            match = pattern.search(text)
            if match:
                line_number = text.count("\n", 0, match.start()) + 1
                errors.append(f"{relative}:{line_number}: {message}; matched value was not printed.")
        for match in EMAIL_RE.finditer(text):
            line_number = text.count("\n", 0, match.start()) + 1
            errors.append(
                f"{relative}:{line_number}: contains an email address in the public repository; "
                "the address was not printed. Use an owner-approved public alias only."
            )


def _check_asset_path(relative: str, errors: list[str]) -> None:
    path = PurePosixPath(relative)
    if not path.parts or path.parts[0] != "assets":
        return
    path_tokens = {
        token
        for part in path.parts
        for token in re.split(r"[^a-z0-9]+", part.lower())
        if token
    }
    sensitive = sorted(path_tokens & SENSITIVE_PATH_PARTS)
    if sensitive:
        errors.append(f"Sensitive path name in public assets: {relative} ({', '.join(sensitive)}).")
    suffix = path.suffix.lower()
    if suffix not in ALLOWED_ASSET_SUFFIXES:
        errors.append(f"Unexpected public asset type: {relative} ({suffix or 'no extension'}).")
    if suffix == ".txt":
        is_font_license = len(path.parts) >= 3 and path.parts[1] == "fonts" and path.name.startswith("OFL-")
        if not is_font_license:
            errors.append(
                f"Unexpected public text asset: {relative}. Only named OFL font licenses are allowed under assets/."
            )


def _local_target(source_relative: str, reference: str) -> tuple[str | None, str | None]:
    reference = reference.strip()
    if not reference:
        return None, None
    if reference.startswith("#"):
        return source_relative, unquote(reference[1:]) or None
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or reference.startswith("//"):
        return None, None

    decoded_path = unquote(parsed.path).replace("\\", "/")
    if not decoded_path:
        return source_relative, unquote(parsed.fragment) or None

    if decoded_path.startswith("/"):
        candidate = PurePosixPath(decoded_path.lstrip("/"))
    else:
        candidate = PurePosixPath(source_relative).parent / decoded_path

    stack: list[str] = []
    for part in candidate.parts:
        if part in {"", "."}:
            continue
        if part == "..":
            if not stack:
                return "<outside-repository>", None
            stack.pop()
        else:
            stack.append(part)
    normalized = PurePosixPath(*stack).as_posix()
    if decoded_path.endswith("/"):
        normalized = (PurePosixPath(normalized) / "index.html").as_posix()
    return normalized, unquote(parsed.fragment) or None


def _check_html(
    relative: str,
    text: str,
    expanded: set[str],
    html_parsers: dict[str, PublicHTMLParser],
    errors: list[str],
) -> None:
    parser = PublicHTMLParser()
    try:
        parser.feed(text)
        parser.close()
    except Exception as exc:  # HTMLParser can surface malformed entity/state errors.
        errors.append(f"{relative}: HTML parse failed: {exc}.")
        return
    html_parsers[relative] = parser

    if parser.h1_count != 1:
        errors.append(f"{relative}: expected exactly one H1, found {parser.h1_count}.")
    if parser.main_count != 1:
        errors.append(f"{relative}: expected exactly one main landmark, found {parser.main_count}.")

    for href in parser.blank_targets_without_noopener:
        errors.append(f"{relative}: target=_blank link lacks rel=noopener ({href}).")

    for document in parser.json_ld_documents:
        if not document:
            errors.append(f"{relative}: empty JSON-LD block.")
            continue
        try:
            json.loads(document)
        except json.JSONDecodeError as exc:
            errors.append(f"{relative}: invalid JSON-LD: {exc}.")

    for _, reference in parser.references:
        target, fragment = _local_target(relative, reference)
        if target is None:
            continue
        if target == "<outside-repository>":
            errors.append(f"{relative}: local reference escapes the repository ({reference!r}).")
            continue
        target_path = REPO_ROOT.joinpath(*PurePosixPath(target).parts)
        if not target_path.is_file():
            errors.append(f"{relative}: missing local reference {reference!r} -> {target}.")
            continue
        if target not in expanded:
            errors.append(f"{relative}: local reference is not in .pages-manifest ({target}).")
        if fragment and target.lower().endswith(".html"):
            # Fragment checks are completed after every HTML file has been parsed.
            pass

    for _, css_reference in CSS_URL_RE.findall(text):
        target, _ = _local_target(relative, css_reference)
        if target is None:
            continue
        target_path = REPO_ROOT.joinpath(*PurePosixPath(target).parts)
        if not target_path.is_file():
            errors.append(f"{relative}: missing CSS URL {css_reference!r} -> {target}.")
        elif target not in expanded:
            errors.append(f"{relative}: CSS URL target is not in .pages-manifest ({target}).")


def _check_css_references(relative: str, text: str, expanded: set[str], errors: list[str]) -> None:
    for _, reference in CSS_URL_RE.findall(text):
        target, _ = _local_target(relative, reference)
        if target is None:
            continue
        target_path = REPO_ROOT.joinpath(*PurePosixPath(target).parts)
        if not target_path.is_file():
            errors.append(f"{relative}: missing CSS URL {reference!r} -> {target}.")
        elif target not in expanded:
            errors.append(f"{relative}: CSS URL target is not in .pages-manifest ({target}).")


def _check_fragments(
    texts: dict[str, str], html_parsers: dict[str, PublicHTMLParser], errors: list[str]
) -> None:
    for relative, parser in html_parsers.items():
        for _, reference in parser.references:
            target, fragment = _local_target(relative, reference)
            if not target or not fragment or not target.lower().endswith(".html"):
                continue
            target_parser = html_parsers.get(target)
            if target_parser is None and target in texts:
                target_parser = PublicHTMLParser()
                target_parser.feed(texts[target])
                target_parser.close()
                html_parsers[target] = target_parser
            if target_parser is not None and fragment not in target_parser.ids:
                errors.append(f"{relative}: missing fragment target {reference!r} in {target}.")


def _check_truth_invariants(
    texts: dict[str, str], html_parsers: dict[str, PublicHTMLParser], errors: list[str]
) -> None:
    for relative, parser in html_parsers.items():
        if relative == "404.html":
            continue
        lowered = texts[relative].lower()
        if "ai-created" not in lowered and "synthetic" not in lowered:
            errors.append(f"{relative}: missing an explicit AI-created/synthetic disclosure.")

    index = texts.get("index.html", "")
    index_parser = html_parsers.get("index.html")
    if index:
        has_music_zero_state = "no song has been released yet" in index.lower()
        verified_release_links = index_parser.verified_release_links if index_parser else []
        if has_music_zero_state and verified_release_links:
            errors.append("index.html: music zero-state and verified-release markers may not coexist.")
        elif not has_music_zero_state and not verified_release_links:
            errors.append(
                "index.html: music must retain the no-release truth statement or use an external HTTPS link "
                "marked data-verifiable-release=\"true\" after evidence exists."
            )

    polls = texts.get("polls.html", "")
    polls_parser = html_parsers.get("polls.html")
    if polls:
        has_poll_zero_state = "no collaborations yet" in polls.lower()
        verified_results = polls_parser.verified_result_markers if polls_parser else 0
        if has_poll_zero_state and verified_results:
            errors.append("polls.html: collaboration zero-state and verified-result markers may not coexist.")
        elif not has_poll_zero_state and not verified_results:
            errors.append(
                "polls.html: retain the no-collaboration zero-state or mark each evidence-backed archive entry "
                "with data-verified-result=\"true\"."
            )

    for relative, text in texts.items():
        if not relative.endswith(".html") or "instagram.com" not in text.lower():
            continue
        parser = html_parsers.get(relative)
        if parser and not parser.verified_instagram_links:
            errors.append(
                f"{relative}: Instagram links require data-verified-account=\"true\" after ownership/public "
                "availability is verified."
            )


def _check_sitemap(errors: list[str]) -> None:
    path = REPO_ROOT / "sitemap.xml"
    if not path.is_file():
        return
    try:
        ElementTree.parse(path)
    except ElementTree.ParseError as exc:
        errors.append(f"sitemap.xml: invalid XML: {exc}.")


def _image_identity(data: bytes) -> tuple[str, int, int]:
    """Return the encoded format and dimensions for supported public images."""

    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24 and data[12:16] == b"IHDR":
        width, height = struct.unpack(">II", data[16:24])
        return "png", width, height

    if data.startswith(b"\xff\xd8"):
        position = 2
        start_of_frame = {
            0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
            0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF,
        }
        while position < len(data):
            while position < len(data) and data[position] != 0xFF:
                position += 1
            while position < len(data) and data[position] == 0xFF:
                position += 1
            if position >= len(data):
                break
            marker = data[position]
            position += 1
            if marker in {0x01, 0xD8, 0xD9} or 0xD0 <= marker <= 0xD7:
                continue
            if position + 2 > len(data):
                break
            segment_length = struct.unpack(">H", data[position:position + 2])[0]
            if segment_length < 2 or position + segment_length > len(data):
                break
            if marker in start_of_frame and segment_length >= 7:
                height, width = struct.unpack(">HH", data[position + 3:position + 7])
                return "jpeg", width, height
            position += segment_length
        raise ValueError("JPEG dimensions could not be decoded")

    if data.startswith(b"RIFF") and len(data) >= 20 and data[8:12] == b"WEBP":
        position = 12
        while position + 8 <= len(data):
            chunk_type = data[position:position + 4]
            chunk_size = struct.unpack("<I", data[position + 4:position + 8])[0]
            payload = data[position + 8:position + 8 + chunk_size]
            if len(payload) != chunk_size:
                break
            if chunk_type == b"VP8X" and len(payload) >= 10:
                width = 1 + int.from_bytes(payload[4:7], "little")
                height = 1 + int.from_bytes(payload[7:10], "little")
                return "webp", width, height
            if chunk_type == b"VP8 " and len(payload) >= 10 and payload[3:6] == b"\x9d\x01\x2a":
                width = struct.unpack("<H", payload[6:8])[0] & 0x3FFF
                height = struct.unpack("<H", payload[8:10])[0] & 0x3FFF
                return "webp", width, height
            if chunk_type == b"VP8L" and len(payload) >= 5 and payload[0] == 0x2F:
                packed = int.from_bytes(payload[1:5], "little")
                width = 1 + (packed & 0x3FFF)
                height = 1 + ((packed >> 14) & 0x3FFF)
                return "webp", width, height
            position += 8 + chunk_size + (chunk_size % 2)
        raise ValueError("WebP dimensions could not be decoded")

    raise ValueError("unsupported or invalid image signature")


def _check_image_provenance(errors: list[str]) -> None:
    """Require a byte-accurate, one-to-one record for every public image."""

    provenance_path = REPO_ROOT / "assets" / "provenance.json"
    image_root = REPO_ROOT / "assets" / "img"
    if not provenance_path.is_file():
        errors.append("Missing assets/provenance.json for public image integrity checks.")
        return
    if not image_root.is_dir():
        errors.append("Missing assets/img directory.")
        return

    try:
        document = json.loads(provenance_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        errors.append(f"assets/provenance.json could not be parsed for image integrity: {exc}.")
        return

    records = document.get("assets") if isinstance(document, dict) else None
    if not isinstance(records, list):
        errors.append("assets/provenance.json: top-level 'assets' must be an array.")
        return

    required_document_fields = {
        "schema_version": str,
        "generated_on": str,
        "site": str,
        "scope": str,
        "provenance_limits": dict,
    }
    for field, field_type in required_document_fields.items():
        if not isinstance(document.get(field), field_type) or not document.get(field):
            errors.append(f"assets/provenance.json: top-level {field!r} is missing or invalid.")
    limits = document.get("provenance_limits")
    if isinstance(limits, dict):
        for field in ("human_direction_and_review", "synthetic_media_disclosed"):
            if limits.get(field) is not True:
                errors.append(f"assets/provenance.json: provenance_limits.{field} must be true.")
        if limits.get("public_derivatives_should_be_assumed_to_retain_source_credentials") is not False:
            errors.append(
                "assets/provenance.json: provenance_limits must explicitly reject assuming retained source credentials."
            )

    actual_paths = {
        path.relative_to(REPO_ROOT).as_posix()
        for path in image_root.rglob("*")
        if path.is_file() and not path.is_symlink()
    }
    records_by_path: dict[str, list[tuple[int, dict[str, object]]]] = {}

    for index, record in enumerate(records):
        record_number = index + 1
        if not isinstance(record, dict):
            errors.append(f"assets/provenance.json: asset record {record_number} must be an object.")
            continue
        raw_path = record.get("path")
        if not isinstance(raw_path, str) or not raw_path.strip():
            errors.append(f"assets/provenance.json: asset record {record_number} has no valid path.")
            continue
        normalized = raw_path.strip().replace("\\", "/")
        pure_path = PurePosixPath(normalized)
        if pure_path.is_absolute() or ".." in pure_path.parts or normalized != pure_path.as_posix():
            errors.append(
                f"assets/provenance.json: asset record {record_number} has a non-normalized or unsafe path."
            )
            continue
        records_by_path.setdefault(normalized, []).append((record_number, record))

    duplicate_paths = sorted(path for path, entries in records_by_path.items() if len(entries) != 1)
    for path in duplicate_paths:
        record_numbers = ", ".join(str(number) for number, _ in records_by_path[path])
        errors.append(
            f"assets/provenance.json: {path} must be listed exactly once; found records {record_numbers}."
        )

    recorded_paths = set(records_by_path)
    missing_records = sorted(actual_paths - recorded_paths)
    extra_records = sorted(recorded_paths - actual_paths)
    if missing_records:
        errors.append("Images missing provenance records: " + ", ".join(missing_records) + ".")
    if extra_records:
        errors.append("Provenance records without matching assets/img files: " + ", ".join(extra_records) + ".")

    for relative in sorted(actual_paths & recorded_paths):
        entries = records_by_path[relative]
        if len(entries) != 1:
            continue
        record_number, record = entries[0]
        image_path = REPO_ROOT.joinpath(*PurePosixPath(relative).parts)

        required_record_fields = {
            "role": str,
            "format": str,
            "width": int,
            "height": int,
            "bytes": int,
            "sha256": str,
            "synthetic_media": bool,
            "public_web_derivative": bool,
            "source_record": str,
        }
        for field, field_type in required_record_fields.items():
            value = record.get(field)
            if type(value) is not field_type or (field_type is str and not value.strip()):
                errors.append(
                    f"assets/provenance.json record {record_number}: {field!r} is missing or invalid."
                )

        if record.get("synthetic_media") is not True or record.get("public_web_derivative") is not True:
            errors.append(
                f"assets/provenance.json record {record_number}: disclosure flags must both be true."
            )
        if record.get("source_record") != "owner-archived":
            errors.append(
                f"assets/provenance.json record {record_number}: source_record must be 'owner-archived'."
            )

        image_data = image_path.read_bytes()
        try:
            actual_format, actual_width, actual_height = _image_identity(image_data)
        except ValueError as exc:
            errors.append(f"assets/provenance.json record {record_number}: {relative}: {exc}.")
        else:
            if record.get("format") != actual_format:
                errors.append(
                    f"assets/provenance.json record {record_number}: format mismatch for {relative}; "
                    f"recorded={record.get('format')!r}, actual={actual_format!r}."
                )
            if record.get("width") != actual_width or record.get("height") != actual_height:
                errors.append(
                    f"assets/provenance.json record {record_number}: dimensions mismatch for {relative}; "
                    f"recorded={record.get('width')!r}x{record.get('height')!r}, "
                    f"actual={actual_width}x{actual_height}."
                )

        expected_bytes = record.get("bytes")
        actual_bytes = image_path.stat().st_size
        if type(expected_bytes) is not int or expected_bytes != actual_bytes:
            errors.append(
                f"assets/provenance.json record {record_number}: byte count mismatch for {relative}; "
                f"recorded={expected_bytes!r}, actual={actual_bytes}."
            )

        expected_sha = record.get("sha256")
        actual_sha = hashlib.sha256(image_data).hexdigest()
        if not isinstance(expected_sha, str) or expected_sha.lower() != actual_sha:
            errors.append(
                f"assets/provenance.json record {record_number}: SHA-256 mismatch for {relative}; "
                f"actual={actual_sha}."
            )


def _build_artifact(expanded: set[str], output: Path, errors: list[str]) -> None:
    output = output if output.is_absolute() else REPO_ROOT / output
    output = output.resolve()
    try:
        relative_output = output.relative_to(REPO_ROOT)
    except ValueError:
        errors.append(f"Artifact output must stay inside the repository: {output}.")
        return
    if relative_output.as_posix() != ".pages-artifact":
        errors.append("Artifact output must be the repository-local .pages-artifact directory.")
        return

    if output.exists():
        if output.is_symlink() or not output.is_dir():
            errors.append("Refusing to replace a non-directory or symlink at .pages-artifact.")
            return
        shutil.rmtree(output)
    output.mkdir(parents=True)

    for relative in sorted(expanded):
        source = REPO_ROOT.joinpath(*PurePosixPath(relative).parts)
        destination = output.joinpath(*PurePosixPath(relative).parts)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    built = {
        path.relative_to(output).as_posix()
        for path in output.rglob("*")
        if path.is_file()
    }
    if built != expanded:
        missing = sorted(expanded - built)
        extra = sorted(built - expanded)
        errors.append(f"Artifact mismatch after copy; missing={missing}, extra={extra}.")


def verify(build_output: Path | None = None) -> list[str]:
    errors: list[str] = []
    _check_repository_document_safety(errors)
    _, expanded = _parse_manifest(errors)
    if not expanded:
        return errors

    _check_manifest_completeness(expanded, errors)

    texts: dict[str, str] = {}
    html_parsers: dict[str, PublicHTMLParser] = {}
    for relative in sorted(expanded):
        _check_asset_path(relative, errors)
        path = REPO_ROOT.joinpath(*PurePosixPath(relative).parts)
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"CNAME", ".nojekyll"}:
            continue
        text = _read_public_text(path, errors)
        if text is None:
            continue
        texts[relative] = text
        _check_public_safety(relative, text, errors)
        if path.suffix.lower() == ".html":
            _check_html(relative, text, expanded, html_parsers, errors)
        elif path.suffix.lower() == ".css":
            _check_css_references(relative, text, expanded, errors)
        elif path.suffix.lower() == ".json":
            try:
                json.loads(text)
            except json.JSONDecodeError as exc:
                errors.append(f"{relative}: invalid JSON: {exc}.")

    _check_fragments(texts, html_parsers, errors)
    _check_truth_invariants(texts, html_parsers, errors)
    _check_sitemap(errors)
    _check_image_provenance(errors)

    if build_output is not None and not errors:
        _build_artifact(expanded, build_output, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--build",
        metavar=".pages-artifact",
        type=Path,
        help="After verification, rebuild the repository-local .pages-artifact directory.",
    )
    args = parser.parse_args()

    errors = verify(args.build)
    if errors:
        print(f"Site verification failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    action = "verified and assembled" if args.build else "verified"
    print(f"Site {action} successfully from .pages-manifest.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
