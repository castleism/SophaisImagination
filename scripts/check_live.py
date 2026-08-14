#!/usr/bin/env python3
"""Compare the deployed Pages site with the current committed public artifact."""

from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
import time
from pathlib import Path, PurePosixPath
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


REPO_ROOT = Path(__file__).resolve().parent.parent
CANONICAL = "https://sophais-imagination.com/"
SKIP_HTTP_COMPARE = {".nojekyll", "CNAME"}
USER_AGENT = "SophiasImaginationReleaseCheck/1.0"


def git_bytes(spec: str) -> bytes:
    result = subprocess.run(
        ["git", "show", spec],
        cwd=REPO_ROOT,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(f"Could not read committed release input {spec}")
    return result.stdout


def committed_tree_files(prefix: str) -> list[str]:
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", "HEAD", "--", prefix],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(f"Could not list committed release directory {prefix}")
    return [line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()]


def manifest_files() -> list[str]:
    files: set[str] = set()
    manifest = git_bytes("HEAD:.pages-manifest").decode("utf-8")
    for raw_line in manifest.splitlines():
        value = raw_line.strip().replace("\\", "/")
        if not value or value.startswith("#"):
            continue
        if value.endswith("/"):
            files.update(committed_tree_files(value.rstrip("/")))
        else:
            files.add(value)
    return sorted(files)


def committed_bytes(relative: str) -> bytes:
    return git_bytes(f"HEAD:{relative}")


def fetch(url: str, timeout: float) -> tuple[bytes, str, int]:
    request = Request(
        url,
        headers={"User-Agent": USER_AGENT, "Cache-Control": "no-cache"},
    )
    with urlopen(request, timeout=timeout) as response:
        return response.read(), response.geturl(), response.status


def encoded_path(relative: str) -> str:
    return "/".join(quote(part) for part in PurePosixPath(relative).parts)


def redirect_errors(timeout: float) -> list[str]:
    errors: list[str] = []
    for source in ("http://sophais-imagination.com/", "https://www.sophais-imagination.com/"):
        try:
            _, final_url, status = fetch(source, timeout)
        except (HTTPError, URLError, TimeoutError) as exc:
            errors.append(f"Redirect check failed for {source}: {exc}")
            continue
        if status != 200 or final_url != CANONICAL:
            errors.append(f"{source} ended at {final_url} with HTTP {status}; expected {CANONICAL}")
    return errors


def branded_404_errors(timeout: float) -> list[str]:
    url = CANONICAL + "release-check-this-page-does-not-exist"
    try:
        fetch(url, timeout)
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        if exc.code != 404:
            return [f"Branded 404 path returned HTTP {exc.code}, not 404"]
        required = ("An imagined page", "most of Sophia's places don't exist")
        return [f"Branded 404 is missing {text!r}" for text in required if text not in body]
    except (URLError, TimeoutError) as exc:
        return [f"Branded 404 check failed: {exc}"]
    return ["Missing page unexpectedly returned a success response"]


def compare_once(files: list[str], timeout: float) -> list[str]:
    errors: list[str] = []
    for relative in files:
        if relative in SKIP_HTTP_COMPARE:
            continue
        expected = committed_bytes(relative)
        url = CANONICAL + encoded_path(relative)
        try:
            actual, final_url, status = fetch(url, timeout)
        except (HTTPError, URLError, TimeoutError) as exc:
            errors.append(f"{relative}: request failed ({exc})")
            continue
        if status != 200:
            errors.append(f"{relative}: HTTP {status}")
            continue
        if final_url != url:
            errors.append(f"{relative}: redirected unexpectedly to {final_url}")
        if actual != expected:
            errors.append(
                f"{relative}: live SHA-256 {hashlib.sha256(actual).hexdigest()} does not match "
                f"HEAD {hashlib.sha256(expected).hexdigest()}"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempts", type=int, default=6, help="Comparison attempts while Pages propagates")
    parser.add_argument("--delay", type=float, default=10.0, help="Seconds between attempts")
    parser.add_argument("--timeout", type=float, default=20.0, help="Per-request timeout")
    args = parser.parse_args()
    if args.attempts < 1 or args.delay < 0 or args.timeout <= 0:
        parser.error("attempts must be positive; delay nonnegative; timeout positive")

    files = manifest_files()
    errors: list[str] = []
    for attempt in range(1, args.attempts + 1):
        errors = redirect_errors(args.timeout)
        errors.extend(branded_404_errors(args.timeout))
        errors.extend(compare_once(files, args.timeout))
        if not errors:
            compared = len([path for path in files if path not in SKIP_HTTP_COMPARE])
            print(f"Live site matches HEAD for {compared} public files; redirects and branded 404 pass.")
            return 0
        if attempt < args.attempts:
            print(f"Attempt {attempt}/{args.attempts} found {len(errors)} issue(s); waiting for propagation.")
            time.sleep(args.delay)

    print(f"Live verification failed with {len(errors)} issue(s):", file=sys.stderr)
    for error in errors:
        print(f"  - {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
