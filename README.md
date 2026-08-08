# Sophia's Imagination — sophais-imagination.com

Official SFW pop-icon / singer page for Sophia (MyPersonas identity `sophai.imagines`). Static single-page site. This is one of Sophia's two pages; the 18+ lane is fully separate and intentionally not linked here.

## Stack

Best practice AND free: static HTML on GitHub Pages with a custom domain — same pattern as the MyPersonas repo. (Paid upgrade path if ever needed: Cloudflare Pages/Pro for CDN analytics + image optimization; not required now.)

## Deploy (one-time owner steps)

1. Create GitHub repo `SophaisImagination`, push this folder to `main`.
2. Settings → Pages → Source: **GitHub Actions**.
3. DNS for `sophais-imagination.com`: apex `A` records → GitHub Pages IPs (185.199.108.153 / .109. / .110. / .111.) and `www` CNAME → `<user>.github.io`. CNAME file is already in the repo.
4. Settings → Pages → enable **Enforce HTTPS** once the cert issues.

## Before adding this URL to any bio (per launch dossier)

- [ ] Verify site is live at https://sophais-imagination.com with HTTPS
- [ ] Owner confirms Instagram @sophais.imagination and X @Sophai_imagines are live and controlled (links in the Official section point there)
- [ ] Review privacy.html + terms.html

## Content rules (from Sophia master prompt + dossier)

- Sophia is always disclosed as a fictional AI-created character; never claim humanity, presence, travel, events, or product use.
- No released music exists → the Music section promises honestly and claims nothing. Do not add players, releases, or "out now" language until real, owned/licensed audio exists.
- No 18+ links on this site. No owner Gmail published. No real-person likeness.
- Castleborn lore stays private; nothing on this site references it.

## Structure

- `index.html` — entire site (styles + JS inline)
- `assets/img/` — web-optimized derivatives of the approved champagne-gold launch set (source: MyPersonas repo `outputs/sophia-social-launch-2026-08-08/`)
- `privacy.html`, `terms.html`, `robots.txt`, `sitemap.xml`, `CNAME`, `.nojekyll`
- `.github/workflows/pages.yml` — Pages deploy on push to `main`

See `ROADMAP.md` for planned work and `CHANGELOG.md` for history.
