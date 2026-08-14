# Roadmap — sophais-imagination.com

Status legend: `[DONE]` `[BLOCKED — OWNER]` `[DELEGATE — OTHER AI]`

## v0.1 — Launch — SHIPPED 2026-08-08

- [DONE] General-audience home page with an always-visible synthetic-media disclosure, promise cards, ten-concept gallery, honest no-release stage, collaboration ritual, official links, privacy, and terms.
- [DONE] GitHub Pages workflow, custom domain, unproxied DNS, HTTPS, sitemap, robots, `.nojekyll`, web derivatives, Open Graph image, and icons.
- [DONE] X profile publicly located. Instagram link withheld because the intended handle could not be verified.

## v0.2 — Depth — SHIPPED 2026-08-09

- [DONE] Process page with human art-direction notes explicitly framed as notes, not machine logs.
- [DONE] Three clearly labeled fictional diary entries.
- [DONE] Series tags: Couture, Imagined Places, Character Studies, Collaborations, and Process.
- [DONE] Collaboration archive with a truthful zero-state and no invented results.
- [DONE] Custom 404, sitemap, and deployment allowlist updates.

## v0.2.1 — Accessibility and image performance — SHIPPED 2026-08-13

- [DONE] Skip links, labeled navigation landmarks, one main/H1 per page, corrected heading hierarchy, footer overflow fix, and passing solid-surface text contrast.
- [DONE] Keyboard-operable gallery buttons; modal initial focus, Tab containment, inert background, Escape/backdrop/close handling, and exact trigger focus return.
- [DONE] Twelve WebP alternatives with JPEG fallback. Supporting-browser payload for the hero, stage image, and ten concepts fell from 1,744,505 to 1,197,134 bytes (31.4%).
- [DONE] Browser QA at 320, 768, and 1440 CSS pixels with zero console errors.
- [DONE] Source commit `dbb2af8`; GitHub Pages run #11 succeeded. All seven then-public HTML files and sampled WebPs matched live; apex/www redirects, DNS, and certificate were healthy.

## v0.2.2 — Trust, privacy, provenance, and release safety — SHIPPED 2026-08-13

- [DONE] Self-hosted official Latin WOFF2 subsets for Cormorant Garamond and Inter with OFL licenses, eliminating Google Fonts requests; privacy copy updated accordingly.
- [DONE] Public-safe provenance page and machine-readable SHA-256/dimension record for every public media derivative in the release, with explicit limits on what hashes and stripped web derivatives prove.
- [DONE] Corrected the diary's future-vote wording; replaced repeated generic image descriptions with concept-specific alt text; completed social-preview metadata; tightened focus/reduced-motion/dialog/footer semantics.
- [DONE] Added no-referrer and practical same-origin meta CSP policies compatible with the static site's inline code.
- [DONE] Replaced the fragile duplicated deploy allowlist with a single manifest plus a zero-dependency source/artifact verifier.
- [DONE] Split build and deploy permissions, pinned official GitHub actions to immutable SHAs, included hidden `.nojekyll` explicitly, and added timeouts.
- [DONE] Added a main-only weekly/manual health workflow that compares every HTTP-comparable committed content file with the live site (excluding the two Pages control files, `.nojekyll` and `CNAME`) and checks redirects plus the branded 404.
- [DONE] Guarded the push helper against private author emails and unsafe automatic lock removal; repository-local author now uses GitHub noreply.
- [DONE] Sanitized current public documentation so it does not expose private operator paths, private source identifiers, or cross-brand boundary details.
- [DONE] Added a release checklist and an empty evidence-first collaboration record template.
- [DONE] Source commit `42513b4`; Pages run #12 succeeded. All 45 HTTP-comparable committed content files matched live byte-for-byte; apex/www redirects, the branded 404, local-font delivery, WebP selection, mobile overflow, and browser console checks passed.

## v0.3 — The first public participation loop — BLOCKED — OWNER

The highest-value next unit is not another speculative site section. It is an approved first substantial X post, followed by one real audience choice and an evidence-backed archive entry.

- [BLOCKED — OWNER] Approve or revise the exact public name/hashtag, gold-and-ivory identity, destination, rights/provenance review, ten-post order, and C01 caption/image/alt text.
- [BLOCKED — OWNER] Verify X write authority and account health. A public profile is not proof of provider access.
- [BLOCKED — OWNER] Create or verify the intended Instagram account before restoring its link or preparing provider actions.
- [BLOCKED — OWNER] Approve a real three-word choice with source URL, close rule, counts, permission-based credit, and correction policy before populating the archive.
- [DONE — LOCAL] Approval-ready decision sheet prepared in the private launch package; queue remains awaiting approval, not queued, externally disabled, and globally paused.

## v0.4 — The Debut — BLOCKED — OWNER

- [BLOCKED — OWNER] No more music generation or credit use until the owner approves one exact story, title, lyric set, adversarial review, disclosure, voice direction, tool, and one-test scope.
- [DELEGATE — OTHER AI] After approval only: one original controlled song test; no imitation of a named artist; full rights, stems, tool/version, prompts, hashes, and disclosure records.
- [BLOCKED — OWNER] Synthetic spoken voice requires separate consent, platform-policy, disclosure, and safety review; never for DMs or simulated human intimacy.
- [DELEGATE — OTHER AI] Motion/visualizer work begins only from owner-approved stills after voice/music decisions; label it synthetic and log provenance.
- [BLOCKED — OWNER] Add release pages or links only after owned/licensed audio exists at a verifiable destination.

## Later depth — evidence-triggered

- [BLOCKED — OWNER] Named visual eras begin only when a second identity is approved and ships.
- [BLOCKED — OWNER] Continue the diary at a quiet monthly cadence when new approved material exists.
- [BLOCKED — OWNER] Add email capture only with a real provider, privacy terms, and a clear subscriber benefit.
- [BLOCKED — OWNER] Add a public rights/impersonation contact only after a dedicated public alias exists.
- [BLOCKED — OWNER] Submit Search Console/Bing verification only through an owner-controlled account.
- [BLOCKED — OWNER] Legal review of ownership/rights wording and a coordinated Git-history privacy rewrite are separate owner decisions.

## Permanent rules

- The honesty is the moat: no fake releases, events, votes, results, collaborations, endorsements, audience numbers, or machine-log claims.
- Keep the site and public repository general-audience and separated from private brands, lore, prompts, paths, and operator data.
- Do not add a framework without a demonstrated need; the static site remains the free, low-risk default.
- Preserve built → approved → pushed → deployed → live-verified as separate states.
