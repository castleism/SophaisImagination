# Delegation Briefs — controlled distribution and catalog growth (v0.4)

Status: ALL future work below is **[BLOCKED — OWNER]** to execute. Four public Suno songs and two YouTube videos already exist; they are audit inputs, not authorization for another generation, render, upload, or release. These briefs exist so work can begin only after the owner approves the exact scope, rights, licensing, and disclosure. Public-safe direction is recorded here; private source material remains in the owner's working archive.

## Brief 1 — Original music (Suno / Udio / human collaborator)

**Potential deliverable:** one controlled song-five test. The owner attests that the correct eligible plan was active for the existing songs; the two additional account-level songs still require general-audience review plus complete private source, rights, and disclosure records. Retain plan/terms corroboration when available for the audit trail. Additional versions or a release require a fresh decision after the test is reviewed.

- Required sequence: concrete story ledger → exact lyrics → adversarial truth/safety review → owner approval of story, title, lyrics, disclosure, voice direction, tool, and one-test credit scope → one render.
- Stop condition: if the concept or test is rejected, do not generate a replacement until the owner approves a revised exact package.

- Style: ethereal pop; cinematic shimmer; subtle choral and crystalline textures; unhurried tempo (~70–95 BPM); elegant restraint over drops.
- Voice: original synthetic voice ONLY — never imitate, clone, or reference any living or deceased singer. No artist style-prompts by name.
- Lyrical lanes (match persona voice: luminous, self-aware, honest): imagined worlds and impossible couture; memory of designed places; transparency as beauty ("honestly synthetic"); the audience as co-creator. No romance-bait, no claims of lived experience, no political lines.
- Hard rules: owner must hold full commercial rights + stems; no samples without license; log tool, version, prompts, and output hashes for provenance; label as AI-created in all metadata and descriptions.
- Definition of done for commercial distribution: owner-approved master + stems + provenance log + written rights confirmation + verified platform disclosure and destination. The Stage may truthfully record a public concept release without implying those commercial gates passed.

## Brief 2 — Synthetic voice identity (blocked hardest — needs owner + policy review)

**Deliverable:** a spoken voice identity for future narration/shorts. Master prompt currently says NO until consent, platform policy, disclosure, and safety review are approved.

- Direction (when unblocked): warm mezzo range, unhurried cadence, precise diction, slight smile; reads like a knowing narrator, not a girlfriend simulator.
- Never: clone a real person, imply live human chat, or use for DMs/replies. Always: AI-voice disclosure wherever used.

## Brief 3 — Motion / video (Runway / Pika / Veo class)

**Deliverable:** after the two existing YouTube videos are reconciled, 6–15s cinematic loops per concept for platform-native posts (9:16 + 1:1 + 16:9).

- Source stills: owner-approved source masters only; keep face geometry, palette, and couture exactly consistent—no identity drift.
- Motion language: slow push-ins, fabric and light movement, starlight parallax, one reveal per clip; no fast cuts; no lip-sync until a voice identity exists.
- Editing rhythm (from master prompt): unhurried opening, one clear transformation or reveal, satisfying final frame, native caption with AI disclosure.
- Rules: label as AI-generated; keep every prompt/seed/version in a provenance log; no real locations implied; platform-safe styling only.

## Brief 4 — Image continuation (next concept batches)

**Deliverable:** new concepts in existing series (Couture / Imagined Places / Character Studies / Collaborations / Process).

- Identity continuity: use only owner-approved source masters and preserve the same clearly adult fictional Sophia, composed couture presentation, and champagne-gold public visual language already visible on the site. Exact private identity-lock specifications stay in the owner's working archive.
- Prohibited: text baked into images, watermarks, celebrity likeness, extra faces, sexualized framing, deceptive documentary styling, minors or age ambiguity — ever.
- Output: destination-appropriate platform crops plus web derivatives, with dimensions recorded in the private approved brief before execution.
- Every batch needs owner review before joining the site catalog.

## Brief 5 — Android packaging of the PWA (TWA) — NOT STARTED, OWNER DECISION FIRST

**Deliverable:** only if the owner decides a Play Store listing is wanted. The site is now an installable PWA, which already covers "put it on my phone" without a store at all — the owner opens `https://sophais-imagination.com` on the device and chooses Install / Add to Home Screen. Do this first and confirm it is not sufficient before anyone builds an APK.

- **Free / no-build route (recommended):** the installed PWA. No Play account, no signing key, no store review, no update lag. Icons, offline page, and standalone display are already in place.
- **Store route (only on owner decision):** Bubblewrap (`@bubblewrap/cli`) or PWABuilder generates a Trusted Web Activity wrapper around the same origin. Requirements the executing model must not skip: a Play Console account, an upload signing key the owner controls and backs up, a `.well-known/assetlinks.json` file served from the apex with that key's SHA-256 fingerprint (without it the app shows a browser address bar), and a Play data-safety declaration.
- **Store-listing honesty rules carry over unchanged:** the listing must state that Sophia is a fictional AI-created character and that the imagery is synthetic. Do not claim releases, results, sponsors, or collaborations that cannot be verified. Do not imply she is human.
- **Cannot be done from the assistant environment:** no Android SDK, no `adb`, no device access. Both the install and any APK build are owner-side actions.

## Handoff protocol

1. Owner approves a brief and provides accounts/licenses.
2. Executing model logs: date, tool + version, prompts/seeds, selected outputs, rejected outputs (sample), hashes.
3. Human owner-editor reviews against the persona's never-say/never-do list.
4. Site and private launch records update together (`ROADMAP.md`, `CHANGELOG.md`, and the owner's approval record).
