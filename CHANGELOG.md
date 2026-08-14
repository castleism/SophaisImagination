# Changelog — sophais-imagination.com

## 2026-08-13 — v0.2.1 (built locally, not published)

- Accessibility: added visible-on-focus skip links to Home, Process, Diary, and Collaboration Archive; added/cleaned main, page-navigation, and footer-navigation landmarks across all seven public pages; corrected the Archive rules heading level.
- Gallery/lightbox: replaced mouse-only card activation with native image buttons; added initial focus, Tab/Shift+Tab containment, inert background content, Escape handling, and exact-trigger focus restoration on every close path.
- Contrast: verified `--muted` at 6.85:1 or better on the site's solid backgrounds; replaced the failing ~3.47:1 copyright color with `--muted`.
- Responsive: fixed footer-link horizontal overflow on Home, Process, Diary, and Collaboration Archive at 320 CSS pixels; tablet (768) and desktop (1440) layouts remained clean.
- Performance: added 12 WebP alternatives (hero, stage, 10 concepts) at unchanged dimensions with JPEG fallbacks. Representative hero/gallery pairs were visually compared and all 12 passed dimension/format checks. They total 1,197,134 bytes as WebP versus 1,744,505 bytes as JPEG, a 547,371-byte / 31.4% reduction for supporting browsers. OG, avatar, favicon, and touch icon formats are unchanged.
- Semantics: gallery series labels now render as block-displayed `<span>` elements before each preserved H3; Process images also use `<picture>` without changing public copy.
- Deploy boundary: `.github/workflows/pages.yml` already includes `assets/***`, so the new WebPs require no allowlist change. No commit, push, Pages deploy, social post, music generation, or account change was performed.
- Live state rechecked 2026-08-13: HTTPS redirects and all seven public pages are healthy; Instagram `@sophais.imagination` remains unavailable publicly; X `@Sophai_imagines` remains at 0 posts and 0 followers.
- Verification: browser DOM/console checks on all seven pages; skip target activation; keyboard checks for lightbox focus containment/return, Escape/close behavior, and mobile menu state; responsive overflow checks at 320/768/1440; WebP selection and fallback dimensions; workflow YAML, sitemap XML, local-reference, JavaScript syntax, and `git diff --check` checks.

## 2026-08-09 — v0.2.0 DEPLOYED (overnight, owner-approved autonomy)

- All 7 deploy files committed to origin via GitHub web UI (base64 → synthetic clipboard paste into the web editor; select-all via synthetic ctrl+a keydown). Each file verified byte-identical vs local using `git show origin/main:<file> | cmp`.
- Local git reconciled: `git reset origin/main`; only repo docs remain as a local commit for the next owner push.

## 2026-08-09 — v0.2.0 (built overnight, pending owner push)

- New pages: `process.html` (art-direction notes ×10), `diary.html` (3 labeled-fiction entries), `polls.html` (collaboration archive, honest zero-state), `404.html`.
- Gallery: series tags added (Couture / Imagined Places / Character Studies / Collaborations / Process) + "deeper" links row; footer links expanded.
- Official Links: Instagram card removed — public check shows @sophais.imagination does not exist; X @Sophai_imagines verified live. Anti-impersonation note reworded.
- Infra: sitemap includes new pages; Pages deploy allowlist includes new pages + 404.
- Docs: `docs/DELEGATION-BRIEFS.md` (music/voice/video/image briefs for other AI models — all execution owner-blocked).
- Tests: 7 pages parse clean; jsdom render checks (10 cards + series tags, 10 process entries, 3 diary entries, 4 poll steps, IG link absent, X link present); all pages HTTP 200 on local serve; sitemap XML + workflow YAML validated. Backups in `_to_delete/backups-2026-08-08/`.

## 2026-08-08 — v0.1.0 deployed (LIVE)

- Repo `castleism/SophaisImagination` created; Pages Source = GitHub Actions; custom domain saved; DNS check passed.
- Cloudflare DNS: 4 apex A records (185.199.108–111.153) + www CNAME → castleism.github.io, all DNS-only.
- Owner pushed via `_ops/push.ps1`; deploy #1 green; Enforce HTTPS enabled; https://sophais-imagination.com verified in browser.

## 2026-08-08 — v0.1.0 (initial build)

- Built complete single-page SFW pop-icon site: hero (Meet Sophia 16:9), always-visible synthetic-media disclosure strip, "What is real / What is fiction" promise cards, 10-concept gallery (approved launch-pack captions) with lightbox, honest no-releases-yet Music section, three-word collaboration ritual, official-links section with anti-impersonation note, privacy and terms pages.
- Name stylization locked for this site: **Sophia's Imagination** (owner choice, 2026-08-08).
- Owner choices: new repo + GitHub Pages; concept-era honest music framing; no 18+ linkage anywhere on site.
- Assets: 16 web derivatives generated from MyPersonas launch set (gallery 800×1067, hero 1600×900, OG 1200×630, favicon/touch icons from avatar). Sources unchanged in MyPersonas repo.
- Infra: GitHub Actions Pages workflow (allowlist artifact rsync, same pattern as MyPersonas), CNAME, robots.txt, sitemap.xml, .nojekyll, .gitignore.
