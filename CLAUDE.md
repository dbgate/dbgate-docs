# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.
Common documentation is in README.md, keep this documentation up-to-date.

## Additional directories

`.claude/settings.json` grants read-only access to sibling repositories that are the source of knowledge for DbGate itself (write/edit is explicitly denied on all of them). Use them for context when writing or updating docs content (features, config options, terminology, changelog entries, etc.):

- `../dbgate` — main DbGate Community application source (some features for Premium/Team Premium are only in `../dbgate-merged`)
- `../dbgate-merged` — main DbGate Premium/Team Premium application source (use this for complete context on features, config options, and changelog entries)
- `../dbgate-lite` — lite edition of DbGate (Solid.js, browser-based)
- `../web-dbgate-io` — dbgate.io marketing site source

When you need context from one of these projects, check its root `README.md` or `CLAUDE.md` first. Read further into the directory only when that isn't enough to answer the question (e.g. specific feature implementation or config option details).

## Localization

The site is multilingual (Hugo translation-by-content-directory). English source lives in `content/en/`; translations in `content/<lang>/`. See the "Localization" section of README.md for the full picture, and `.claude/skills/translation/SKILL.md` for the translation rules.

**Edit English only.** Write new or updated docs in `content/en/`, then run the `translation` skill to propagate. Never hand-edit a translated file to fix English content — the change would be overwritten on the next sync, since translations are regenerated from the English `sourceHash`.

**Two invariants that Hugo will not enforce for you:**

- **Translated files must never contain an `aliases:` key.** Aliases are legacy *English* URLs. Hugo does not language-prefix them (that only happens on `IsMultihost` sites), so a translated page carrying a copied alias silently takes over the English redirect — `/maps/` would start serving Czech — and the build still exits 0 with no warning. After any translation work: `grep -rl "^aliases:" content/cs/` must return nothing.
- **A language belongs in `hugo.toml` only once its content exists.** A configured language with an empty `contentDir` falls back to English and publishes untranslated duplicates under its prefix.

The `hugo-theme-relearn` submodule supplies all UI strings and ships translations for every configured language except Slovak, so there is no project-level `i18n/` directory yet. The `translation` skill's toml/yml code paths are guarded and inert here (this repo has no `data/` dir and no `i18n/en.toml`); they are kept only so the script stays diffable against `../web-dbgate-io`, where they are live.
