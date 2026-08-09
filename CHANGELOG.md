# Changelog — sophais-imagination.com

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
