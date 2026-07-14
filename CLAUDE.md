# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is the [Hugo](https://gohugo.io/) static-site source for the DbGate documentation, published at https://dbgate.io/. It contains no application code — only Markdown content, a small set of theme overrides, and site config. The visual theme (`hugo-theme-relearn`) is a git submodule, not vendored source.

## Commands

Prerequisite: [Hugo extended](https://gohugo.io/installation/) (project currently builds with v0.140.x) and Node/yarn.

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

## Architecture

- **`content/`** — all documentation pages, one Markdown file per page. Directories (`admin/`, `data-tools/`, `installation/`) become site sections and each needs an `_index.md` for the section landing page. Ordering within the left nav is controlled by the `weight` front matter field (lower = earlier), not by filename or directory order — check sibling files' `weight` when adding a new page to slot it correctly.
- **`layouts/`** — thin overrides/additions on top of the `hugo-theme-relearn` submodule theme:
  - `layouts/partials/` overrides theme partials (`custom-header.html`, `favicon.html`, `logo.html`).
  - `layouts/shortcodes/` defines custom Hugo shortcodes used throughout `content/`: `{{< mdi "icon-name" >}}` (Material Design Icons), `{{< check >}}` (checkmark, used in the database support matrix), `{{< center >}}` (centers content, e.g. table headers).
- **`themes/hugo-theme-relearn/`** — git submodule; do not edit directly. Theme-level look-and-feel changes belong in `assets/css/theme-dbgate.css` (the `dbgate` theme variant referenced by `themeVariant` in `hugo.toml`) or in the `layouts/` overrides above.
- **`hugo.toml`** — site config. Notable: `markup.goldmark.renderer.unsafe = true` (raw HTML in Markdown is allowed), `sitemap.exclude = ["purchase"]`, theme variant is `dbgate`.
- **`static/`** — files served as-is at the site root (favicon, screenshots referenced from content, MDI font files copied in by the `postinstall` yarn script — don't hand-edit `static/mdi/`).
- Images referenced from `content/*.md` are mostly hotlinked from `https://media.dbgate.io/img/...` rather than stored in this repo; a smaller set of local screenshots lives under `static/img/` and `static/screenshots/`.

## Additional directories

`.claude/settings.json` grants read-only access to sibling repositories that are the source of knowledge for DbGate itself (write/edit is explicitly denied on all of them). Use them for context when writing or updating docs content (features, config options, terminology, changelog entries, etc.):

- `../dbgate` — main DbGate application source
- `../dbgate-merged` — merged/combined DbGate source variant
- `../dbgate-lite` — lite edition of DbGate (Solid.js, browser-based)
- `../web-dbgate-io` — dbgate.io marketing site source

When you need context from one of these projects, check its root `README.md` or `CLAUDE.md` first. Read further into the directory only when that isn't enough to answer the question (e.g. specific feature implementation or config option details).

## Deployment

Two CI paths exist:
- `.github/workflows/azure-static-web-apps-ambitious-pebble-0eed14903.yml` — active workflow, builds with `yarn install && hugo` and deploys to Azure Static Web Apps on push/PR to `master`.
- `.github/workflows/hugo.yaml.bak` — disabled (`.bak`) GitHub Pages deployment workflow, kept for reference.

Both build against the submodule theme, so a PR that updates `themes/hugo-theme-relearn` must commit the new submodule commit pointer, and CI must check out with submodules enabled (already configured in both workflows).
