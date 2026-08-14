# Sophia's Imagination — sophais-imagination.com

Official general-audience site for Sophia, a fictional AI-created pop icon and muse. The site is intentionally transparent: the imagination and human art direction are real; the character biography and depicted worlds are fiction.

## Current state

- Live at <https://sophais-imagination.com> with HTTPS enforced.
- GitHub Pages deploys from `main` through GitHub Actions.
- v0.2.1 was verified live on 2026-08-13 at source commit `dbb2af8` and Actions run #11.
- Instagram remains absent from Official Links because the intended public handle has not been verified.
- X is linked publicly, but publishing authority is not inferred from the existence of the account.

## v0.2.2 release candidate

The working tree contains an unreleased v0.2.2 candidate. It adds same-site fonts,
public derivative provenance, stronger accessibility and privacy behavior, and a
manifest-driven verifier and deployment artifact. Those changes are not described
as live until the release checklist, Pages run, and post-deploy byte comparison pass.

## Stack

Hand-written static HTML, CSS, and JavaScript; no framework, package manager,
analytics, cookies, database, or build dependency. In the v0.2.2 candidate, fonts
and media are served from the same site. A small standard-library verification
script checks source and deployment artifacts.

## Deployment

The repository is already configured. Normal release flow:

1. Run the local verifier documented in `docs/RELEASE-CHECKLIST.md`.
2. Commit with the repository-local GitHub noreply identity.
3. Run `.\_ops\push.ps1` from the repository root.
4. Confirm the Pages workflow succeeds, then verify the live site, redirects, and representative assets.

The Pages artifact is controlled by `.pages-manifest`. Any new public root file must be added there. Public assets must remain under the explicitly allowed `assets/` directories and pass the verifier.

## Content rules

- Always disclose Sophia as a fictional AI-created character. Never imply humanity, consciousness, physical presence, travel, events, product use, or real-world relationships.
- No released music exists. Do not add players, releases, streaming links, dates, or “out now” language until owned/licensed audio exists verifiably.
- Keep the site and this public repository strictly general-audience.
- Do not publish private operator details, private source paths, unpublished lore, prompts, rejected assets, or personal email addresses.
- No real-person likeness or voice without written consent; no imitation of a named living artist.
- Never invent votes, audience counts, collaborations, endorsements, testimonials, or provenance evidence.

## Structure

The entries below describe the v0.2.2 candidate repository, including files that
are not yet part of the verified-live v0.2.1 site.

- `index.html` — home, disclosure, gallery, honest music zero-state, collaboration prompt, and official links
- `process.html` — art-direction notes for the ten concepts
- `diary.html` — clearly labeled fictional character diary
- `polls.html` — collaboration archive with an honest zero-state
- `provenance.html` — public-safe media provenance explanation and hash record
- `404.html`, `privacy.html`, `terms.html`, `robots.txt`, `sitemap.xml`
- `assets/img/` — web derivatives; `assets/fonts/` — self-hosted OFL-licensed font subsets
- `assets/provenance.json` — machine-readable hashes and dimensions for public media
- `docs/DELEGATION-BRIEFS.md` — owner-gated v0.3 briefs
- `.pages-manifest` and `.github/workflows/` — verified Pages artifact definition, deployment, and read-only live-health monitoring
- `scripts/verify_site.py`, `scripts/check_live.py`, and `_ops/push.ps1` — local verification, live comparison, and guarded push helpers

See `ROADMAP.md` for status and `CHANGELOG.md` for release history.
