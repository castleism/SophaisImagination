# Roadmap — sophais-imagination.com

Status legend: [DONE] [READY] [BLOCKED — OWNER] [DELEGATE — OTHER AI]

## v0.1 — Launchable SFW pop-icon page

- [DONE] 2026-08-08 — Single-page site: hero, disclosure strip, promise, 10-concept gallery with lightbox, honest Music/"The Stage" section, three-word collaboration ritual, official links, footer, privacy, terms.
- [DONE] 2026-08-08 — Web-optimized image set (16 files, ~1.9 MB total), OG image, favicons.
- [DONE] 2026-08-08 — Pages workflow, CNAME, robots, sitemap, .nojekyll.
- [DONE] 2026-08-08 — GitHub repo `castleism/SophaisImagination` created (public); Pages Source = GitHub Actions; custom domain sophais-imagination.com saved in Pages settings.
- [DONE] 2026-08-08 — Cloudflare DNS: 4 apex A records (185.199.108-111.153) + www CNAME → castleism.github.io, all DNS-only (required for GitHub cert issuance). Local git remote wired; `_ops/push.ps1` helper added.
- [DONE] 2026-08-08 — Owner pushed via `_ops/push.ps1`; Pages deploy #1 succeeded (23s); DNS check passed; Enforce HTTPS enabled; site verified live at https://sophais-imagination.com (hero, disclosure, gallery, all sections rendering).
- [DONE] 2026-08-09 — Handle verification (public check): X @Sophai_imagines EXISTS (display "Sophia", joined Dec 2025, 0 posts — matches inventory/backup). Instagram @sophais.imagination DOES NOT EXIST publicly ("page isn't available") → IG link REMOVED from Official Links until the owner creates/renames the account. [OWNER] Recreate or confirm IG handle, then restore the card in index.html.

**v0.1 SHIPPED 2026-08-08.**

## v0.2 — Depth — BUILT 2026-08-09, awaiting owner push to deploy

- [DONE] Process page (`process.html`): art-direction notes for all 10 concepts (seed language / design notes / what was kept / formats). Honest framing: design notes, not machine logs; provenance stays owner-archived.
- [DONE] Character diary (`diary.html`): 3 entries in Sophia's voice, "Labeled fiction" chip, per-entry honesty asides; Entry One expands the staged "Character Diary One" concept.
- [DONE] Series system (v1 of eras): all 10 concepts tagged Couture / Imagined Places / Character Studies / Collaborations / Process on the gallery + process page. Named visual eras start when a second visual identity ships (crystal/lavender is the candidate per master prompt — owner decision).
- [DONE] Collaboration archive (`polls.html`): honest zero-state (no invented results), 4-step how-it-works, append-only archive rules.
- [DONE] Custom 404 page; sitemap + deploy allowlist updated for all new pages.
- [DONE] 2026-08-09 — v0.2 DEPLOYED overnight via GitHub web-UI commits (owner approved full autonomy; no CLI credentials needed): pages.yml `d004be4`, process `951b808`, diary `4c0cc3a`, polls `69dab52`, 404 `02137f8`, sitemap `f77e124`, index `58eb79d`. Every file verified byte-identical between origin and local via `git show | cmp`. Local repo reconciled to origin.
- [OWNER — next push] Repo docs (README/ROADMAP/CHANGELOG/docs/) ride along with the next `.\_ops\push.ps1`.

**v0.2 SHIPPED 2026-08-09.**

## v0.3 — The debut (all BLOCKED — OWNER until real assets exist)

- Original song(s): [DELEGATE — OTHER AI] music generation (e.g., Suno/Udio or human collaborator) — owner must resolve licensing, voice identity, and disclosure before anything is embedded. Brief for the model: ethereal pop, cinematic shimmer, subtle choral/crystalline textures; no imitation of any living singer.
- Voice identity: [DELEGATE — OTHER AI] synthetic voice design — blocked on owner approval per master prompt (§ AI voice: no until consent/policy/safety review).
- Lyric visuals / visualizer video: [DELEGATE — OTHER AI] video model (e.g., Runway/Pika/Veo) using the champagne-gold visual lock; label as synthetic.
- Release page with verifiable links only after audio actually exists.

## Open owner decisions carried from master prompt

- Final public stylization confirmed as "Sophia's Imagination" for this site (chosen 2026-08-08 in build session).
- girlgamerswp gaming account role — not referenced on this site until decided.
- Newer four-asset Sophia/Tiamaria reference pack is [REF, NOT SHIP] and lives outside this repo; not used.
