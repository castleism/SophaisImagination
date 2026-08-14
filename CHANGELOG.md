# Changelog — sophais-imagination.com

## 2026-08-13 — v0.2.2 (built; release verification pending)

- Privacy/resilience: replaced Google Fonts requests with three self-hosted Latin WOFF2 subsets (125,156 bytes total), preserved exact weight/style matching, and included both SIL OFL 1.1 license texts plus source hashes.
- Provenance: added a public-safe explanation page and machine-readable record of filename, format, dimensions, byte size, and SHA-256 for every public media derivative in the candidate. The copy explicitly distinguishes byte identity from private source records, rights, and content credentials.
- Correctness/accessibility: corrected the diary's premature vote wording; added factual concept-specific image descriptions; expanded visible-focus and reduced-motion support; tightened dialog/footer semantics; added async image decoding where safe.
- Metadata/privacy: completed Open Graph/Twitter image metadata, added a no-referrer policy, and added a practical same-origin meta CSP compatible with current inline styles/scripts.
- Deployment safety: introduced one public artifact manifest and zero-dependency source/live verifiers; split build/deploy permissions; pinned official GitHub actions to immutable release SHAs; preserved `.nojekyll`; added timeouts and a main-only weekly/manual live-health check.
- Repository privacy: set the local author to GitHub noreply, added future-author/privacy checks, stopped automatic Git-lock deletion, and sanitized current public documentation. Older public commits still require a separately approved history rewrite if they are to be removed.
- Operations: added a release checklist and empty evidence-first collaboration record template. Prepared a separate local social decision sheet without altering approval, queue, pause, account, or publishing state.

## 2026-08-13 — v0.2.1 DEPLOYED

- Accessibility: added visible-on-focus skip links to Home, Process, Diary, and Collaboration Archive; added/cleaned main, page-navigation, and footer-navigation landmarks across all seven public pages; corrected the Archive rules heading level.
- Gallery/lightbox: replaced mouse-only card activation with native image buttons; added initial focus, Tab/Shift+Tab containment, inert background content, Escape handling, and exact-trigger focus restoration on every close path.
- Contrast: verified `--muted` at 6.85:1 or better on the site's solid backgrounds; replaced the failing ~3.47:1 copyright color with `--muted`.
- Responsive: fixed footer-link horizontal overflow on Home, Process, Diary, and Collaboration Archive at 320 CSS pixels; tablet (768) and desktop (1440) layouts remained clean.
- Performance: added 12 WebP alternatives (hero, stage, 10 concepts) at unchanged dimensions with JPEG fallbacks. Representative hero/gallery pairs were visually compared and all 12 passed dimension/format checks. They total 1,197,134 bytes as WebP versus 1,744,505 bytes as JPEG, a 547,371-byte / 31.4% reduction for supporting browsers. OG, avatar, favicon, and touch icon formats are unchanged.
- Semantics: gallery series labels now render as block-displayed `<span>` elements before each preserved H3; Process images also use `<picture>` without changing public copy.
- Deploy boundary: `.github/workflows/pages.yml` included `assets/***`, so the new WebPs required no allowlist change.
- Live state rechecked 2026-08-13: HTTPS redirects and all seven public pages are healthy; Instagram `@sophais.imagination` remains unavailable publicly; X `@Sophai_imagines` remains at 0 posts and 0 followers.
- Verification: source commit `dbb2af8`; GitHub Pages run #11 succeeded. All seven then-public HTML files and sampled WebPs matched live. Browser DOM/console checks covered skip target activation, lightbox focus containment/return, Escape/close behavior, mobile menu state, overflow at 320/768/1440, WebP selection, workflow YAML, sitemap XML, local references, JavaScript syntax, and `git diff --check`.

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

- Built complete single-page SFW pop-icon site: hero (Meet Sophia 16:9), always-visible synthetic-media disclosure strip, "What is real / What is fiction" promise cards, 10-concept gallery (selected review-package captions) with lightbox, honest no-releases-yet Music section, three-word collaboration ritual, official-links section with anti-impersonation note, privacy and terms pages.
- Name stylization locked for this site: **Sophia's Imagination** (owner choice, 2026-08-08).
- Owner choices: new repo + GitHub Pages; concept-era honest music framing; general-audience public scope.
- Assets: 16 initial web derivatives from the owner-provided review set (gallery 800×1067, hero 1600×900, OG 1200×630, favicon/touch icons from avatar). This historical site selection does not imply social-package or rights approval; source records remain in the owner's private archive.
- Infra: GitHub Actions Pages workflow with an allowlisted artifact, CNAME, robots.txt, sitemap.xml, `.nojekyll`, and `.gitignore`.
