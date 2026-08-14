# Release checklist

Use this for every public site change. Built, approved, pushed, deployed, and live-verified are separate states.

## Before the commit

- [ ] Confirm the active repository and current branch.
- [ ] Back up every touched existing file under `_to_delete/backups-YYYY-MM-DD-<scope>/`.
- [ ] Confirm the change contains no private email, absolute local path, credentials, prompts, rejected assets, private lore, or non-general-audience material.
- [ ] Add every new public root file to `.pages-manifest`; keep public assets within its allowed directories.
- [ ] Update page metadata, sitemap dates, `assets/provenance.json`, `ROADMAP.md`, and `CHANGELOG.md` when affected.
- [ ] Run `python scripts/verify_site.py`.
- [ ] Inspect `git diff --check`, the complete staged diff, and the intended author email.

## Publish

- [ ] Commit with a focused message and the repository-local GitHub noreply identity.
- [ ] Record the rollback SHA (`git rev-parse HEAD^`).
- [ ] Push with `.\_ops\push.ps1`; clear a lock only after confirming no Git process is active and using its explicit safety switch.
- [ ] Confirm the source branch contains the intended commit.
- [ ] Confirm the GitHub Pages run succeeds with no unexpected warning.

## Live verification

- [ ] Confirm apex HTTP redirects to apex HTTPS.
- [ ] Confirm `www` resolves to the apex HTTPS site.
- [ ] Check every public HTML route plus one real 404 path.
- [ ] Confirm title, H1, disclosure, no-release text, and no-vote state.
- [ ] Confirm representative WebP, JPEG fallback, font, and provenance JSON requests.
- [ ] Compare live bytes or hashes with the release artifact for changed files.
- [ ] Run `python scripts/check_live.py` after Pages reports success; it compares every HTTP-comparable committed content file except `.nojekyll` and `CNAME`, plus redirects and the branded 404.
- [ ] Confirm the main-only live-health workflow remains enabled; its weekly check is read-only and does not replace release verification.
- [ ] Perform keyboard and responsive smoke checks for any affected interaction.
- [ ] Mark the release shipped in `ROADMAP.md` and `CHANGELOG.md` only after these checks pass.

## External-state reminder

Site deployment never proves social-account ownership, provider write access, post publication, analytics, music rights, or search-engine indexing. Verify each separately.
