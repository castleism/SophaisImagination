# Roadmap — sophais-imagination.com

Status legend: `[DONE]` `[DONE — LOCAL]` `[OWNER-ATTESTED]` `[EVIDENCE — REVIEW]` `[BLOCKED — OWNER]` `[DELEGATE — OTHER AI]`

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

The highest-value next unit is not another speculative site section. It is an approved identity/campaign post that corrects the currently disclosure-thin feed, followed by one bounded audience choice and an evidence-backed archive entry.

- [BLOCKED — OWNER] Approve or revise the exact public name/hashtag, gold-and-ivory identity, destination, rights/provenance review, ten-post order, and C01 caption/image/alt text.
- [BLOCKED — OWNER] Verify X write authority and account health. A public profile is not proof of provider access.
- [BLOCKED — OWNER] Reconcile the intended unavailable Instagram spelling with the differently spelled owner-controlled account; approve its public name, synthetic disclosure, site link, and exact official status before restoring a website link.
- [BLOCKED — OWNER] Decide whether the owner-published YouTube channel belongs to this public-safe identity or a separate story lane. Do not list it as official until its name, disclosure, outbound link, and public-safe positioning are approved.
- [BLOCKED — OWNER] Correct or replace the current X travel-framed music post and disclosure-thin profiles/posts. The existing permanent posts are not C01 and do not constitute a vote.
- [BLOCKED — OWNER] Reconcile two additional public Suno songs and all public voice/profile labels against the general-audience, adult-only, rights, and disclosure rules. Do not imply the whole account catalog is approved.
- [BLOCKED — OWNER] Approve the first bounded choice with a source URL, close rule, eligibility/count rules, permission-based credit, and correction policy before populating the archive; approve the later Three-Word Worlds submission ritual separately.
- [DONE — LOCAL] The immutable 30-item review bundle was re-fingerprinted on 2026-08-26; all five bundle hashes and C01's image hash still match. The queue remains awaiting approval, not queued, externally disabled, and marked as requiring a global pause. The actual provider pause must be verified privately before staging.
- [DONE — LOCAL] The three flagged visuals were re-reviewed at full size: C06's waterfalls descend into cloud/mist, C10's crystal treatment is architectural but fully clothed, and Facebook C03 remains fully clothed. Acceptance remains an owner choice.
- [DONE — LOCAL] A refreshed private gate card and a no-invented-results participation protocol were prepared without editing the immutable queue.

## v0.3.0 — The Stage opens — SHIPPED 2026-08-19

- [DONE] Two songs were published on Suno on 2026-08-16 by the owner: **"Sophia's Fall"** and **"The Ancestors Are Us"**. The public song pages show a synthetic voice profile and model version; private source identifiers remain outside this repository.
- [DONE] The Stage replaced its false no-release state with the two verifiable Suno song pages. Source commit `bb76480`; Pages run #14 succeeded. On 2026-08-26, all 45 public files matched live and the August 24 health run was green.
- [DONE — LOCAL] The next local patch removes the now-false "Suno only" and absolute Official Links claims after the official X account linked YouTube uploads. It also attributes creation/no-sampling statements to the owner-editor and states their evidentiary limit.
- [DONE — LOCAL] After two additional Suno songs and unresolved account-level identity material were found, the next local artifact withholds Suno and X profile cards. No provider content was deleted or changed.
- [DONE — LOCAL] After owner-editor story-boundary review, the next local artifact retains both original owner-published songs in the general-audience Stage. No removal or unlisting action is recommended for either reviewed song.
- [OWNER-ATTESTED] The owner confirms that the correct eligible plan was active when the songs were created. Retain dated plan and applicable-terms records privately when available as audit corroboration; their absence does not make the owner's plan knowledge unknown. Do not publish billing details.
- [DONE — LOCAL] A public-safe audio provenance record was started for both reviewed song links and their observed public metadata; all owner-only source fields remain explicitly incomplete.
- [BLOCKED — OWNER] Before a new commercial use, approve the exact use and complete the substantive private record: source/master hashes, lyrics versions, tool settings, voice/source authorization, stems/downloads, and any collaborators or uploaded material. Retain plan/terms corroboration when available as supporting audit evidence.

## v0.3.1 — Supporting-page metadata — SHIPPED 2026-09-23

- [DONE] Added descriptions and self-canonical URLs to privacy and terms while retaining their deliberate `noindex` state. Source commit `753de4d`; Pages run `35925135241` succeeded.
- [DONE] Read-only verification on 2026-09-24 matched all 45 HTTP-comparable public files to `753de4d`; internal references, key assets, apex/www redirects, sitemap, robots, and the branded 404 passed.
- [DONE — LOCAL] The unreleased truth-state patch now sits cleanly on top of `753de4d`; it does not regress the supporting-page metadata.

## v0.4 — Controlled distribution and catalog growth — BLOCKED — OWNER

- [BLOCKED — OWNER] Further music generation and credit use requires the owner to approve the exact story, title, lyric set, adversarial review, disclosure, voice direction, tool, and scope per song. Four songs are now public on the linked Suno account; this gate governs song five onward.
- [DELEGATE — OTHER AI] After approval only: one controlled song-five test; no imitation of a named artist; full rights, stems, tool/version, prompts, hashes, and disclosure records.
- [BLOCKED — OWNER] Synthetic spoken voice requires separate consent, platform-policy, disclosure, and safety review; never for DMs or simulated human intimacy.
- [BLOCKED — OWNER] Reconcile and disclose the two existing YouTube videos before additional motion/visualizer work. Future motion begins only from owner-approved stills and retains source/provenance records.
- [BLOCKED — OWNER] Add Spotify, Apple Music, sales, paid EP, or other commercial-distribution links only after rights and delivery evidence are archived and approved.

## Six-year business path — PLANNING ONLY

No revenue engine is verified as active. The supplied portfolio ranges are proposals, not forecasts, and do not authorize a checkout, provider, purchase, post, outreach, distribution submission, or account change.

- [DONE — LOCAL] Added `REVENUE-MODEL.md` with an evidence-gated first-dollar sequence and separate Year 1, Year 2, and Years 3–6 operating horizons. Internal audience and financial targets are not reproduced in this public repository.
- [DONE — LOCAL] Added `docs/COMMERCE-READINESS.md`. The ten 800 × 1067 catalog files are web derivatives, not print masters or sale-ready inventory.
- [BLOCKED — OWNER] A first print proof requires one approved source master, complete private rights review, provider/product/price approval, and a proof budget. A shop requires additional seller, tax, payment, fulfillment, support, privacy, shipping, and refund decisions plus an end-to-end test.
- [BLOCKED — OWNER] Brand collaboration, virtual-fashion licensing, sync, paid music distribution, and a paid MyPersonas page each require their own written scope and external-system approvals.

| Horizon | Proposed focus |
| --- | --- |
| Year 1 | Finish identity and rights gates; prove one print before any limited pilot; continue approved editorial/music work |
| Year 2 | One disclosed collaboration; couture licensing; controlled rights-cleared distribution |
| Years 3–6 | Evidence-led virtual fashion, music catalog, and approved platform presence |

Internal audience and revenue targets remain private owner-review inputs, not public claims or forecasts.

**Pivot rules:** identity repair and the first evidence-backed participation loop stay ahead of commerce. If no approved source master and private rights record exist, no print proof begins. If a proof fails, revise only with exact approval or return to editorial work. Before a pilot opens, the owner must set acceptable margin, defect, refund/replacement, and support-load thresholds; pause rather than expand when any threshold fails or remains unmeasured.

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
