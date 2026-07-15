#!/usr/bin/env python3
"""Stamp the English source hash into a freshly translated file.

Idempotent: removes any existing hash markers first, then writes the current one,
so it is safe to run after either a full or an incremental translation.

Usage:
  python .claude/skills/translation/set_hash.py <md|toml|yml> <out_path> <en_path> [lang]

  md   -> inserts `sourceHash:` and `language:` lines just after the opening `---`
  toml -> prepends `# sourceHash: <hash>` as the first line
  yml  -> prepends `# sourceHash: <hash>` as the first line
"""

import sys
import hashlib


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def stamp_md(out_path, hash_value, lang):
    with open(out_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if not lines or lines[0].strip() != '---':
        raise SystemExit(f'{out_path}: missing opening front-matter "---"')
    # find closing --- of front matter
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end = i
            break
    if end is None:
        raise SystemExit(f'{out_path}: missing closing front-matter "---"')
    body_fm = [ln for ln in lines[1:end]
               if not ln.startswith('sourceHash:') and not ln.startswith('language:')]
    new_lines = (['---\n', f'sourceHash: {hash_value}\n', f'language: {lang}\n']
                 + body_fm + lines[end:])
    with open(out_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)


def stamp_comment(out_path, hash_value):
    with open(out_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines = [ln for ln in lines if not ln.startswith('# sourceHash:')]
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f'# sourceHash: {hash_value}\n')
        f.writelines(lines)


def main():
    if len(sys.argv) < 4:
        raise SystemExit(__doc__)
    kind, out_path, en_path = sys.argv[1], sys.argv[2], sys.argv[3]
    lang = sys.argv[4] if len(sys.argv) > 4 else ''
    hash_value = sha256_file(en_path)
    if kind == 'md':
        if not lang:
            raise SystemExit('md requires a lang argument')
        stamp_md(out_path, hash_value, lang)
    elif kind in ('toml', 'yml'):
        stamp_comment(out_path, hash_value)
    else:
        raise SystemExit(f'unknown kind: {kind}')
    print(f'stamped {out_path} ({hash_value[:12]}…)')


if __name__ == '__main__':
    main()
