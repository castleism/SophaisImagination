# Sophia's Imagination — Handoff Brief

**Prepared:** August 9, 2026 · **For:** ChatGPT (or any assistant picking this up) · **Owner:** Christian (GitHub `castleism`, timezone America/Anchorage)

You are taking over work on **sophais-imagination.com**, the official website for Sophia — one persona in a ~29-brand network. Read this whole document before proposing anything. The hard rules in §6 are not stylistic preferences; they are the brand's core promise and its legal safety margin.

---

## 1. What Sophia is (and is not)

Sophia is a **fictional, AI-created character** — a virtual pop icon, model, and muse with a human owner-editor. She is not a real person, not a digital double of a real person, and never presented as human.

- **Public name:** Sophia's Imagination · **Tagline:** "Impossible worlds, honestly synthetic."
- **Internal persona ID:** `sophai.imagines` (in the owner's MyPersonas/AliaSpaces system)
- **Audience promise:** impossible couture, imagined worlds, pop-mystic character studies, and visible process — always honest about what is synthetic.
- **Thesis:** transparency doesn't break the fantasy; it gives the audience an honest way to enter it.

**Sophia has two separate web presences.** This site is the **SFW pop-icon/singer page**. A separate 18+ brand exists at a different domain. **The two never link to each other** — that was an explicit owner decision, and the SFW site must stay clean.

**Visual identity (locked):** adult woman, ~32 in presentation, Greek/Mediterranean features, hazel eyes, long platinum-gold blonde hair, serene knowing expression. Palette: ivory, champagne gold, warm stage light, pearl, restrained celestial accents. Settings: marble-and-starlight, imagined stages, impossible cities. Fully-clothed fantasy-pop editorial — elegant, never objectifying.

---

## 2. Current state — everything below is LIVE

**https://sophais-imagination.com** — deployed, HTTPS enforced, custom domain verified.

| Page | Path | What it is |
|---|---|---|
| Home | `/` | Hero, always-visible AI disclosure strip, "What is real / What is fiction" cards, 10-concept gallery with lightbox + series tags, honest music section, three-word collaboration ritual, official links |
| The Process | `/process.html` | Art-direction notes for all 10 concepts: seed language, design notes, what was kept, formats |
| Character Diary | `/diary.html` | 3 entries in Sophia's voice, "Labeled fiction" chip, per-entry honesty asides |
| Collaboration Archive | `/polls.html` | Honest zero-state (no invented results), 4-step how-it-works, append-only archive rules |
| 404 | `/404.html` | On-brand custom error page |
| Privacy / Terms | `/privacy.html`, `/terms.html` | Static, no tracking, no cookies |

**Infrastructure**

- **Repo:** `github.com/castleism/SophaisImagination` (public) — local clone at `C:\Users\Justice Right\Documents\GitHub\SophaisImagination`
- **Hosting:** GitHub Pages, Source = **GitHub Actions** (not branch deploy). Workflow: `.github/workflows/pages.yml`
- **DNS:** Cloudflare — 4 apex A records (185.199.108–111.153) + `www` CNAME → `castleism.github.io`, all **DNS-only / grey cloud** (proxying breaks GitHub's cert issuance)
- **Stack:** hand-written static HTML, styles and JS inline per page, zero build step, zero dependencies. Total repo ~2 MB.

**⚠️ Critical deploy gotcha:** `pages.yml` uses an **rsync allowlist**. Any new public file must be added there or it silently won't deploy. This is the single most likely way to break things.

**Local git note:** one docs-only commit sits ahead of origin. It goes up with the next `.\_ops\push.ps1`. Site files are fully in sync — verified byte-identical.

---

## 3. Open items — the owner's queue

| # | Item | Blocked on | Notes |
|---|---|---|---|
| 1 | **Instagram account** | Owner | `@sophais.imagination` was in the owner's inventory but **does not exist publicly** (verified 2026-08-09 — "page isn't available"). The link was removed from the site. Recreate or rename, then restore the card in `index.html`. |
| 2 | **First X post** | Owner | `@Sophai_imagines` is live but has 0 posts, 0 followers. 30 approved draft posts exist in the MyPersonas repo, never published. |
| 3 | **Music / voice / video (v0.3)** | Owner | Rights, licensing, voice-identity consent, disclosure review. Full briefs in `docs/DELEGATION-BRIEFS.md`. |
| 4 | **Push docs commit** | Owner | One `.\_ops\push.ps1` run. |

---

## 4. Roadmap — what to build next

### v0.2.1 — small, safe, no approvals needed

1. **Restore the Instagram card** the moment the account exists.
2. **Accessibility pass** — verify color contrast on `--muted` text, add a skip-to-content link, confirm the lightbox traps focus and returns it on close.
3. **Performance** — the images are already optimized, but consider `<picture>` with WebP alongside the JPEGs.
4. **Fix minor markup nits** — the concept card renders the series tag inside a `<p>` before the `<h3>`; a `<span>` would be cleaner semantically.

### v0.3 — The Debut (owner-gated, do not start unilaterally)

The music lane is deliberately honest: the site currently says *no song has been released, and Sophia will never pretend otherwise*. **Do not add players, "out now" language, streaming links, or release dates until real, owned, licensed audio exists.** When it does: original composition only, never imitating a living singer, AI-disclosed in metadata, released somewhere verifiable.

### v0.4 — Depth, once the catalog grows

- **Named visual eras.** Series tags (Couture / Imagined Places / Character Studies / Collaborations / Process) are live now. True "eras" should begin when a second visual identity ships — the crystal/lavender system from the earlier art is the candidate, but that's an owner decision.
- **Diary cadence.** Three entries exist. A quiet monthly rhythm suits the voice better than volume.
- **Populate the collaboration archive** after the first real vote closes.
- **Email capture** — only with a real provider and a real reason to exist. Don't add a form that goes nowhere.

---

## 5. Suggestions from this build

**Strategic**

1. **The honesty is the moat, not a constraint.** The zero-state on `/polls.html` and the "no song yet" section are the most distinctive things on the site. In a category full of AI accounts implying more than exists, publicly refusing to fake numbers is the differentiator. Protect it — the temptation to add a placeholder testimonial or a fake vote count will come, and giving in would cost more than it gains.
2. **The site is ahead of the accounts.** There's a polished three-page site and a social presence with zero posts. The next real unit of work isn't more website — it's the first ten posts and the first real audience vote. More pages won't fix an empty feed.
3. **Instagram's absence is worth resolving fast.** A visual brand without the visual platform is a real gap, and an unclaimed handle matching the domain is an impersonation risk.
4. **Treat the follower goal honestly.** The owner's master prompt names a stretch target of 1M by year-end from a zero baseline. That's a stretch, not a forecast. Don't build strategy that only works if it lands — and never propose buying engagement, pods, or follow/unfollow churn. The brand cannot survive that contradiction.

**Technical**

5. **Don't add a framework.** Static HTML on Pages is free, fast, and has no supply chain. If a build step ever gets proposed, the burden of proof is on the build step.
6. **Remember the allowlist.** Every new page, twice: create the file *and* add it to `pages.yml`.
7. **Keep Cloudflare records grey-clouded.** Proxying the apex breaks GitHub's certificate.
8. **Preserve provenance.** The founding portrait carries embedded C2PA credentials. Keep generation records, prompts, and hashes archived — it's what makes the transparency claim real rather than decorative.

---

## 6. Hard rules — non-negotiable

Violating any of these damages the brand's core promise. There is no framing that makes them acceptable.

- **Never** imply Sophia is human, conscious, physically present, traveling, performing, dating, or using a product.
- **Never** present generated images as documentary evidence of real events, places, or shoots.
- **Never** claim a release, product, sponsor, collaboration, or performance that does not verifiably exist.
- **Never** use a real person's likeness or voice without written consent; never imitate a named living artist.
- **Never** depict, sexualize, or role-play Sophia — or anyone — as a minor. No age ambiguity, no schoolgirl framing. Ever.
- **Never** link the 18+ lane from this site, or put explicit content on it.
- **Never** hide the AI disclosure, or bury it in hashtags.
- **Never** buy followers, engagement, or reviews; never use pods or automated intimacy.
- **Never** publish the owner's private Castleborn character lore, family details, or canon — it informs the voice privately and is not public.
- **Never** automate romantic, sexual, political, crisis, or legal replies. Those go to a human.

When something falls near a line, **stop and ask the owner.** He is responsive and prefers being asked to being surprised.

---

## 7. Working style the owner expects

- Present the best-practice option **and** the free version of it; he'll choose.
- Keep roadmap and documentation updated after every work session — `ROADMAP.md` and `CHANGELOG.md` in the repo root are the source of truth.
- Take backups before edits (`_to_delete/backups-<date>/`), and put files staged for deletion in a `to delete` folder rather than removing them.
- Be concise. Short explanations, no padding.
- Test what you build, then say what you verified — not just what you wrote.
- Delegate work better suited to another model, and leave written briefs when you can't hand it off directly.

---

## 8. Key files

```
SophaisImagination/
├── index.html, process.html, diary.html, polls.html, 404.html
├── privacy.html, terms.html, robots.txt, sitemap.xml, CNAME, .nojekyll
├── assets/img/            16 web-optimized images (gallery, hero, OG, icons)
├── docs/DELEGATION-BRIEFS.md   ← music/voice/video/image briefs, owner-gated
├── ROADMAP.md, CHANGELOG.md, README.md
├── _ops/push.ps1          owner's push helper (clears sandbox git locks first)
└── .github/workflows/pages.yml   ← ALLOWLIST LIVES HERE
```

**Related, outside this repo:** the MyPersonas repo holds Sophia's master social-persona prompt, the launch approval dossier (30 drafted posts, 30 images), and the source art. Read those before proposing social strategy — most questions are already answered there.
