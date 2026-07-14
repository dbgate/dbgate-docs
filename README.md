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

- **`content/`** — all documentation pages, one Markdown file per page. The site home page (`content/_index.md`) is a product picker. Top-level entries are the products: `dbgate-classic/` (the desktop/self-hosted app — `getting-started/`, `working-with-data/`, `database-operations/`, `customization/`, `admin/`, `developer/` categories plus `dbgate-cloud.md` nested underneath), and the hosted products `dbgate-lite.md`, `dbgate-central/`, `dbgate-shopify-app.md`. A section directory needs an `_index.md` for its landing page, and can nest further sections (e.g. `dbgate-classic/getting-started/installation/`, `dbgate-central/`). Ordering within the left nav is controlled by the `weight` front matter field (lower = earlier), not by filename or directory order. Pages moved between categories carry an `aliases:` front matter entry pointing at their old URL, so existing links keep working.
- **`layouts/`** — thin overrides/additions on top of the `hugo-theme-relearn` submodule theme:
  - `layouts/partials/` overrides theme partials (`custom-header.html`, `favicon.html`, `logo.html`).
  - `layouts/shortcodes/` defines custom Hugo shortcodes used throughout `content/`: `{{< mdi "icon-name" >}}` (Material Design Icons), `{{< check >}}` (checkmark, used in the database support matrix), `{{< center >}}` (centers content, e.g. table headers).
- **`themes/hugo-theme-relearn/`** — git submodule; do not edit directly. Theme-level look-and-feel changes belong in `assets/css/theme-dbgate.css` (the `dbgate` theme variant referenced by `themeVariant` in `hugo.toml`) or in the `layouts/` overrides above.
- **`hugo.toml`** — site config. Notable: `markup.goldmark.renderer.unsafe = true` (raw HTML in Markdown is allowed), `sitemap.exclude = ["purchase"]`, theme variant is `dbgate`.
- **`static/`** — files served as-is at the site root (favicon, screenshots referenced from content, MDI font files copied in by the `postinstall` yarn script — don't hand-edit `static/mdi/`).

Images referenced from `content/*.md` are mostly hotlinked from `https://media.dbgate.io/img/...` rather than stored in this repo; a smaller set of local screenshots lives under `static/img/` and `static/screenshots/`.

## Deployment

Two CI paths exist:
- `.github/workflows/azure-static-web-apps-ambitious-pebble-0eed14903.yml` — active workflow, builds with `yarn install && hugo` and deploys to Azure Static Web Apps on push/PR to `master`.
- `.github/workflows/hugo.yaml.bak` — disabled (`.bak`) GitHub Pages deployment workflow, kept for reference.

Both build against the submodule theme, so a PR that updates `themes/hugo-theme-relearn` must commit the new submodule commit pointer, and CI must check out with submodules enabled.
