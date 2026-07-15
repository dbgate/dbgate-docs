---
name: translation
description: Translate the Hugo docs site (content/en/**/*.md) into all supported languages using local Claude subagents. Incremental — skips files whose sourceHash is unchanged, and patches only changed paragraphs in articles. Use when the user asks to translate the docs, sync translations, or translate a specific page/language. Optional args narrow scope: a language code (cs,de,fr,es,sk,zh,pt,it,ja,ko), a path substring, and/or a type (md).
---

# Docs translation (local Claude agent)

Translating is done by **local Claude subagents** — no API key. It is incremental:
unchanged files are skipped by hash, and changed articles are patched
paragraph-by-paragraph to save time and tokens.

Always run from the repository root: `c:\jenasoft\dbgate-docs`.

This is a port of the same skill in `../web-dbgate-io`. Keep the two in sync where
practical — `translate_plan.py` and `set_hash.py` are intentionally near-identical
so fixes flow both ways.

## Supported languages
`cs` Czech · `de` German · `fr` French · `es` Spanish · `sk` Slovak ·
`zh` Simplified Chinese · `pt` Portuguese (Brazil) · `it` Italian · `ja` Japanese · `ko` Korean

A language is only *published* once it has an entry in `hugo.toml`. Adding content
under `content/<lang>/` without that entry does nothing; adding the entry without
content publishes untranslated English duplicates under the prefix. Do both together.

## Step 1 — Build the work plan

Parse the user's args into optional filters and run the planner:

```
python .claude/skills/translation/translate_plan.py [--lang cs,de] [--path working-with-data] [--type md]
```

- A bare language code in the args → `--lang`.
- Any other token (e.g. `working-with-data/`, a filename, a slug) → `--path`.
- `md` → `--type`.
- No args → full site (every language, every file) = 560 jobs.

The planner prints JSON: `summary`, `deletions` (stale translation files to remove),
and `jobs`. Each job has `type`, `mode`, `lang`, `lang_name`, `en_path`, `out_path`,
`en_hash`, and `base_rev`. **Save the JSON to a file** (e.g. `Write` it to
`.translation-plan.json`) so subagents can read individual jobs without you holding
the whole list in context.

## Step 2 — Confirm scope

Report `summary.jobs` and the per-language / per-type breakdown.

- If **jobs > 25 and the user gave no filter**, do NOT translate everything blindly —
  show the breakdown and ask whether to proceed with the full run or narrow scope
  (each job is a subagent call; a full run is a large token spend).
- If scope is small or the user already specified a filter, proceed.

## Step 3 — Deletions

For every path in `deletions`, delete it (the English source was removed or marked
`skipTranslation: true`). Use `rm`/`Remove-Item`.

## Step 4 — Translate (one subagent per job)

Spawn subagents with the **Agent** tool (subagent_type `general-purpose`), in parallel
waves of up to ~8 at a time. Give each subagent its single job object and the rules
below. The subagent **writes the output file and stamps the hash itself** — it must NOT
return the translated content to you (that would waste tokens). Tell it to return only
a one-line status.

After writing/editing the output file, every subagent finishes by stamping the hash:

```
python .claude/skills/translation/set_hash.py md <out_path> <en_path> <lang>
```

(`set_hash.py` is idempotent — it removes any old hash markers first.)

### Universal translation rules
- Translate natural-language text only. Never translate or alter:
  - Hugo shortcodes `{{< … >}}`, `{{ … }}`, `{{% … %}}` — this site uses
    `{{< mdi "icon-name" >}}`, `{{< check >}}`, `{{< center "text" >}}`. The
    **argument of `center` is display text and IS translated**; `mdi` icon names
    are not.
  - anchor links `[text](#anchor)`, code blocks/spans, HTML tag names/attributes
  - placeholders, URLs of images (`![](...)`, `<img src>`) — images are not
    language-specific and are served from a shared path
- Preserve all Markdown/HTML structure, indentation, and quoting exactly.
- Keep the same quote style (single vs double) as the source.
- Keep DbGate product/edition names untranslated: DbGate, DbGate Cloud, DbGate Central,
  Community, Premium, Team Premium. Database and vendor names too (MySQL, PostgreSQL…).

### md jobs (`content/en/…` → `content/<lang>/…`)

**Front matter:**
- Translate only `title` (and `subtitle`, which exists on one page).
- Keep `weight`, `icon`, `edition`, `demo_url`, `layout` and any other field unchanged.
  `weight` drives nav order and must stay identical to English.
- Keep YAML valid — quote any value containing a colon.
- **`aliases:` — delete the entire `aliases:` block from translated files.**
  Aliases are legacy *English* URLs. Hugo does **not** language-prefix them (it only
  does so for `IsMultihost` sites, which this is not), so a verbatim copy silently
  hijacks the English redirect: the translated page takes over `/maps/`, the prefixed
  route is never created, and **the build still exits 0 with no warning**. Which
  language wins depends on build order, so it shifts as languages are added.
  Translations must never contain an `aliases:` key. See Step 5's guard.

**Body links:** for internal **root-relative** links (`](/dbgate/…)`), prepend the
language code → `](/cs/dbgate/…)`. Leave relative links (`](../dbgate-central/)`)
alone — they already resolve correctly under the language prefix. Do not change
image paths.

Note `content/en/dbgate/customization/env-variables.md` links to `/features/administration`,
which lives on the **web-dbgate-io** site, not here. Prefixing is still correct
(`/cs/features/administration` exists there). Do not convert links to `relref` — it
would fail the build on that cross-site link.

**Modes:**
- **mode `new`** — read `en_path`, translate the whole file per the rules, write to
  `out_path`, then `set_hash.py md <out_path> <en_path> <lang>`.
- **mode `changed` with `base_rev`** — run `git diff <base_rev> -- <en_path>` to see
  exactly what changed in the English since the translation was last made. Read the
  existing `out_path`. Apply the *equivalent* translated changes with `Edit`, touching
  only the affected paragraphs/fields. Leave everything else verbatim. Then `set_hash.py`.
- **mode `changed` without `base_rev`** — read `en_path` and the existing `out_path`.
  The translation is structurally parallel (same headings/order). Compare block by block;
  re-translate with `Edit` only the blocks whose translation no longer matches the English.
  Leave matching blocks untouched. Then `set_hash.py`.

### toml / yml jobs
This repo has no `data/` dir and no project-level `i18n/en.toml` — the relearn theme
supplies all UI strings, and it ships translations for every supported language except
**`sk`**. So the planner emits no toml/yml jobs today; those code paths are guarded and
inert, kept only for parity with web-dbgate-io.

If Slovak is rolled out, add a project-level `i18n/sk.toml` seeded from
`themes/hugo-theme-relearn/i18n/en.toml` (~47 keys; Hugo merges project i18n over theme
i18n). Once an `i18n/en.toml` exists, the toml job type reactivates on its own.

## Step 5 — Verify, then report

**The alias guard is mandatory after any md run** — it is the only thing standing in for
the build error Hugo does not give you:

```bash
# MUST return nothing:
grep -rl "^aliases:" content/cs/

# generalized across all languages — an alias not prefixed with its own lang code is a hijack:
for d in content/*/; do l=$(basename "$d"); [ "$l" = en ] && continue
  grep -rhoE '^\s+- /\S+' "$d" 2>/dev/null | grep -v "^  - /$l/" && echo "HIJACK RISK in $l"
done
```

Then `hugo` and confirm: the build is WARN/ERROR-free, English `Aliases` count is
unchanged (26 — 25 content aliases plus Hugo's generated `/en/` → `/` redirect), and
`<out>/maps/index.html` still redirects to an English target (`grep -o 'url=[^"]*'`
must not contain a language prefix).

Summarize: files created, files patched, files deleted, per language. If any subagent
failed, list those jobs so they can be retried. Finally delete the temporary
`.translation-plan.json`.

## Notes
- The hash format is identical to web-dbgate-io's, so the two repos' skills behave the same.
- `skipTranslation: true` in an English article's front matter excludes it (and causes
  existing translations to be deleted). A translated file with `skipTranslation: true` is
  protected from deletion.
- `set_hash.py` also stamps a `language:` field. It is inert under
  translation-by-directory but is kept for parity with web-dbgate-io.
