# dbgate-docs

[Hugo](https://gohugo.io/) static-site source for the DbGate documentation, published at [dbgate.io](https://dbgate.io/). This repo contains no application code — only Markdown content, a small set of theme overrides, and site config. The visual theme ([`hugo-theme-relearn`](https://github.com/McShelby/hugo-theme-relearn)) is a git submodule, not vendored source.

## Prerequisites

- [Hugo extended](https://gohugo.io/installation/) (currently builds with v0.140.x)
- Node.js and yarn

## Getting started

```bash
# first-time setup / after pulling — fetches the theme submodule
git submodule update --init --recursive

# install JS deps (pulls in @mdi/font icons and copies them into static/mdi via postinstall)
yarn install

# local dev server with live reload, served at http://localhost:1313
hugo server

# production build — output goes to public/
hugo --gc --minify
```

There is no lint, test, or typecheck command in this repo — it's Markdown content plus Hugo templates.

## Project structure

- **`content/<lang>/`** — all documentation pages, one Markdown file per page, one directory per language (`content/en/` is the English source; see [Localization](#localization)). The site home page (`content/en/_index.md`) is a product picker. Top-level entries are the products: `dbgate/` (the desktop/self-hosted app — `getting-started/`, `working-with-data/`, `database-operations/`, `customization/`, `admin/`, `developer/` categories plus `dbgate-cloud.md` nested underneath), and the hosted products `dbgate-lite.md`, `dbgate-central/`, `dbgate-shopify-app.md`. A section directory needs an `_index.md` for its landing page, and can nest further sections (e.g. `dbgate/getting-started/installation/`, `dbgate-central/`). Ordering within the left nav is controlled by the `weight` front matter field (lower = earlier), not by filename or directory order. Pages moved between categories carry an `aliases:` front matter entry pointing at their old URL, so existing links keep working. **Aliases belong to English only and must never appear in a translated file** — Hugo does not language-prefix them, so a copied alias silently steals the English redirect and the build still succeeds. See [Localization](#localization).
- **`layouts/`** — thin overrides/additions on top of the `hugo-theme-relearn` submodule theme:
  - `layouts/partials/` overrides theme partials (`custom-header.html`, `favicon.html`, `logo.html`).
  - `layouts/shortcodes/` defines custom Hugo shortcodes used throughout `content/`: `{{< mdi "icon-name" >}}` (Material Design Icons), `{{< check >}}` (checkmark, used in the database support matrix), `{{< center >}}` (centers content, e.g. table headers).
- **`themes/hugo-theme-relearn/`** — git submodule; do not edit directly. Theme-level look-and-feel changes belong in `assets/css/theme-dbgate.css` (the `dbgate` theme variant referenced by `themeVariant` in `hugo.toml`) or in the `layouts/` overrides above.
- **`hugo.toml`** — site config. Notable: `markup.goldmark.renderer.unsafe = true` (raw HTML in Markdown is allowed), `sitemap.exclude = ["purchase"]`, theme variant is `dbgate`, and the `[languages]` block (see [Localization](#localization)).
- **`static/`** — files served as-is at the site root (favicon, screenshots referenced from content, MDI font files copied in by the `postinstall` yarn script — don't hand-edit `static/mdi/`).

Images referenced from `content/<lang>/**/*.md` are mostly hotlinked from `https://media.dbgate.io/img/...` rather than stored in this repo; a smaller set of local screenshots lives under `static/img/` and `static/screenshots/`. Images are shared across languages — translations never rewrite image paths.

## Localization

The site is multilingual, using Hugo's native translation-by-content-directory and the same conventions as the sibling `../web-dbgate-io` repo. English is the source language; every other language is a machine translation of it.

- **Languages** — configured in the `[languages]` block of `hugo.toml`, each with its own `contentDir`. Currently **English (`en`)** and **Czech (`cs`)**. The remaining targets, with weights reserved to match web-dbgate-io, are `de` 30, `fr` 40, `es` 50, `sk` 60, `zh` 70, `pt` 80, `it` 90, `ja` 100, `ko` 110. **Add a language to `hugo.toml` only once its content is actually translated** — a language with an empty `contentDir` falls back to English and publishes untranslated duplicates under its prefix.
- **URLs** — `defaultContentLanguageInSubdir = false`, so English stays at the root (`/dbgate/...`) and translations are prefixed (`/cs/dbgate/...`). Existing English URLs and inbound links are unaffected.
- **UI chrome** — supplied by the `hugo-theme-relearn` submodule, which ships translations for every configured language except **Slovak**. There is no project-level `i18n/` directory; if `sk` is added, create `i18n/sk.toml` seeded from the theme's `i18n/en.toml` (Hugo merges project i18n over theme i18n). The language switcher, per-language search index, and `lang` attribute are all automatic.
- **hreflang** — emitted by `layouts/partials/custom-header.html` (the theme emits none of its own).

### Translating

Run the `translation` Claude Code skill (`.claude/skills/translation/`), which translates via local Claude subagents — no API key. It is incremental: each translated file stores a `sourceHash` of its English source, so unchanged pages are skipped and changed ones are patched paragraph-by-paragraph.

```bash
# what needs (re)translating — JSON work plan, deterministic, no network
python .claude/skills/translation/translate_plan.py [--lang cs] [--path working-with-data] [--type md]
```

Then invoke the skill (e.g. `/translation cs`) to execute the plan. See `.claude/skills/translation/SKILL.md` for the full rules.

Two invariants matter when touching translations:

1. **Translations must never contain an `aliases:` key.** Aliases are legacy *English* URLs. Hugo only language-prefixes aliases on `IsMultihost` sites, which this is not — so a copied alias silently overrides the English redirect (e.g. `/maps/` starts serving the Czech page) and **the build still exits 0 with no warning**. Guard: `grep -rl "^aliases:" content/cs/` must return nothing.
2. **Root-relative internal links get the language prefix** (`](/dbgate/x)` → `](/cs/dbgate/x)`); relative links (`](../foo/)`) and image paths are left alone.

## Deployment

Two CI paths exist:
- `.github/workflows/azure-static-web-apps-ambitious-pebble-0eed14903.yml` — active workflow, builds with `yarn install && hugo` and deploys to Azure Static Web Apps on push/PR to `master`.
- `.github/workflows/hugo.yaml.bak` — disabled (`.bak`) GitHub Pages deployment workflow, kept for reference.

Both build against the submodule theme, so a PR that updates `themes/hugo-theme-relearn` must commit the new submodule commit pointer, and CI must check out with submodules enabled.
