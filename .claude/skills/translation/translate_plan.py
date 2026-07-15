#!/usr/bin/env python3
"""Scan source (English) files and emit a JSON work plan for the translation skill.

Deterministic, no network. Decides *what* needs translating by comparing the
sha256 of each English source against the `sourceHash` stored in the existing
translation. For incremental work it also figures out the minimal unit:

  - toml: the exact set of keys that are missing or whose English value changed
  - md / yml: whether the file is brand new ("new") or merely changed ("changed");
              for "changed" the subagent applies only the diffed paragraphs.

Run from the repository root:  python .claude/skills/translation/translate_plan.py
Output: a JSON object on stdout (see keys below).
"""

import os
import sys
import json
import argparse
import hashlib
import subprocess

# Same languages as translation/common.py
LANGUAGES = {
    'cs': 'Czech',
    'de': 'German',
    'fr': 'French',
    'es': 'Spanish',
    'sk': 'Slovak',
    'zh': 'Simplified Chinese',
    'pt': 'Portuguese (Brazil)',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def walk(root, ext):
    out = []
    for base, _dirs, names in os.walk(root):
        for name in names:
            if name.endswith(ext):
                full = os.path.join(base, name)
                out.append(os.path.relpath(full, root).replace('\\', '/'))
    return out


# ---------- markdown front matter ----------

def md_front_matter(path):
    fm = {'sourceHash': None, 'skipTranslation': False}
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    i = 0
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    if i >= len(lines) or lines[i].strip() != '---':
        return fm
    for line in lines[i + 1:]:
        if line.strip() == '---':
            break
        if ':' not in line:
            continue
        k, v = line.split(':', 1)
        k, v = k.strip(), v.strip()
        if k == 'sourceHash':
            fm['sourceHash'] = v
        elif k == 'skipTranslation':
            fm['skipTranslation'] = v.lower() == 'true'
    return fm


# ---------- toml / yml stored hash (leading "# sourceHash:" comment) ----------

def comment_hash(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('# sourceHash:'):
                return line.split(':', 1)[1].strip()
            # hash, if present, is on the very first line
            break
    return None


# ---------- toml key parsing ----------

def parse_toml_keys(text):
    """Return {section_key: raw_value_text}. Sections look like `[key]` then `other=...`."""
    keys = {}
    current = None
    for line in text.splitlines():
        s = line.strip()
        if s.startswith('[') and s.endswith(']'):
            current = s[1:-1]
            keys.setdefault(current, '')
        elif current is not None and s.startswith('other'):
            keys[current] = s
    return keys


def git_show(rev_path):
    try:
        out = subprocess.run(['git', 'show', rev_path], capture_output=True, text=True, encoding='utf-8')
        if out.returncode == 0:
            return out.stdout
    except Exception:
        pass
    return None


def git_show_bytes(rev_path):
    try:
        out = subprocess.run(['git', 'show', rev_path], capture_output=True)
        if out.returncode == 0:
            return out.stdout
    except Exception:
        pass
    return None


_base_rev_cache = {}


def find_base_rev(path, target_hash):
    """Find the most recent commit whose version of `path` hashes to target_hash.

    That commit is the English source the existing translation was based on, so a
    diff between it and the current file yields exactly the paragraphs to retranslate.
    Returns a commit SHA, or None if no historical version matches.
    """
    if not target_hash:
        return None
    cache_key = (path, target_hash)
    if cache_key in _base_rev_cache:
        return _base_rev_cache[cache_key]
    result = None
    try:
        log = subprocess.run(['git', 'log', '--format=%H', '--', path],
                             capture_output=True, text=True, encoding='utf-8')
        revs = log.stdout.split()[:80] if log.returncode == 0 else []
        for rev in revs:
            blob = git_show_bytes(f'{rev}:{path}')
            if blob is not None and hashlib.sha256(blob).hexdigest() == target_hash:
                result = rev
                break
    except Exception:
        result = None
    _base_rev_cache[cache_key] = result
    return result


def main():
    ap = argparse.ArgumentParser(description='Emit a translation work plan as JSON.')
    ap.add_argument('--lang', help='comma-separated language codes to limit to (e.g. cs,de)')
    ap.add_argument('--path', help='only include jobs whose en_path contains this substring')
    ap.add_argument('--type', help='comma-separated types to include: md,toml,yml')
    args = ap.parse_args()

    global LANGUAGES
    if args.lang:
        wanted = {c.strip() for c in args.lang.split(',') if c.strip()}
        LANGUAGES = {k: v for k, v in LANGUAGES.items() if k in wanted}
    types = {t.strip() for t in args.type.split(',')} if args.type else None
    path_filter = args.path

    plan = {'languages': LANGUAGES, 'deletions': [], 'jobs': []}

    # ===== Markdown articles =====
    en_md_root = 'content/en'
    en_md = {}
    for rel in walk(en_md_root, '.md'):
        full = os.path.join(en_md_root, rel)
        fm = md_front_matter(full)
        en_md[rel] = {'hash': sha256_file(full), 'skip': fm['skipTranslation']}

    # ===== YAML data =====
    # dbgate-docs has no data/ dir; the code path is kept (guarded) so this file
    # stays diffable against web-dbgate-io, where it is live.
    en_yml_root = 'data/en'
    en_yml = {}
    if os.path.isdir(en_yml_root):
        for rel in walk(en_yml_root, '.yml'):
            full = os.path.join(en_yml_root, rel)
            en_yml[rel] = {'hash': sha256_file(full)}

    # ===== TOML i18n (single source file) =====
    # dbgate-docs has no i18n/en.toml yet (the relearn theme supplies all UI
    # strings). Guarded for the same reason as data/ above; toml jobs stay inert
    # until a project-level i18n/en.toml exists.
    en_toml = 'i18n/en.toml'
    en_toml_has = os.path.exists(en_toml)
    toml_hash = sha256_file(en_toml) if en_toml_has else None
    en_toml_keys = {}
    en_changed_keys = []
    if en_toml_has:
        with open(en_toml, 'r', encoding='utf-8') as f:
            en_toml_text = f.read()
        en_toml_keys = parse_toml_keys(en_toml_text)
        old_toml_text = git_show('HEAD:i18n/en.toml')
        old_toml_keys = parse_toml_keys(old_toml_text) if old_toml_text else {}
        # keys whose English value changed since HEAD (or are brand new in en)
        en_changed_keys = [k for k, v in en_toml_keys.items()
                           if old_toml_keys.get(k) != v]

    for lang, lang_name in LANGUAGES.items():
        # ---- markdown deletions: lang files with no (translatable) en source ----
        lang_md_root = f'content/{lang}'
        if os.path.isdir(lang_md_root):
            for rel in walk(lang_md_root, '.md'):
                lang_file = os.path.join(lang_md_root, rel)
                lang_fm = md_front_matter(lang_file)
                if lang_fm['skipTranslation']:
                    continue
                if rel not in en_md or en_md[rel]['skip']:
                    plan['deletions'].append(lang_file.replace('\\', '/'))

        # ---- markdown jobs ----
        for rel, info in en_md.items():
            if info['skip']:
                continue
            en_path = os.path.join(en_md_root, rel).replace('\\', '/')
            out_path = os.path.join(lang_md_root, rel).replace('\\', '/')
            base_rev = None
            if not os.path.exists(out_path):
                mode = 'new'
            else:
                stored = md_front_matter(out_path)['sourceHash']
                if stored == info['hash']:
                    continue
                mode = 'changed'
                base_rev = find_base_rev(en_path, stored)
            plan['jobs'].append({
                'type': 'md', 'lang': lang, 'lang_name': lang_name,
                'en_path': en_path, 'out_path': out_path,
                'mode': mode, 'en_hash': info['hash'], 'base_rev': base_rev,
            })

        # ---- yml jobs ----
        for rel, info in en_yml.items():
            en_path = os.path.join(en_yml_root, rel).replace('\\', '/')
            out_path = os.path.join(f'data/{lang}', rel).replace('\\', '/')
            base_rev = None
            if not os.path.exists(out_path):
                mode = 'new'
            else:
                stored = comment_hash(out_path)
                if stored == info['hash']:
                    continue
                mode = 'changed'
                base_rev = find_base_rev(en_path, stored)
            plan['jobs'].append({
                'type': 'yml', 'lang': lang, 'lang_name': lang_name,
                'en_path': en_path, 'out_path': out_path,
                'mode': mode, 'en_hash': info['hash'], 'base_rev': base_rev,
            })

        # ---- toml job (incremental, key-level) ----
        if not en_toml_has:
            continue
        out_toml = f'i18n/{lang}.toml'
        if not os.path.exists(out_toml):
            plan['jobs'].append({
                'type': 'toml', 'lang': lang, 'lang_name': lang_name,
                'en_path': en_toml, 'out_path': out_toml,
                'mode': 'new', 'en_hash': toml_hash,
                'keys': sorted(en_toml_keys.keys()),
                'removed_keys': [],
            })
        elif comment_hash(out_toml) != toml_hash:
            with open(out_toml, 'r', encoding='utf-8') as f:
                lang_keys = parse_toml_keys(f.read())
            missing = [k for k in en_toml_keys if k not in lang_keys]
            # union of (changed in en) + (missing in this lang), keep en order
            need = [k for k in en_toml_keys if k in missing or k in en_changed_keys]
            removed = [k for k in lang_keys if k not in en_toml_keys]
            if not need and not removed:
                # hash drifted but nothing substantive changed: just refresh hash
                plan['jobs'].append({
                    'type': 'toml', 'lang': lang, 'lang_name': lang_name,
                    'en_path': en_toml, 'out_path': out_toml,
                    'mode': 'rehash', 'en_hash': toml_hash,
                    'keys': [], 'removed_keys': [],
                })
            else:
                plan['jobs'].append({
                    'type': 'toml', 'lang': lang, 'lang_name': lang_name,
                    'en_path': en_toml, 'out_path': out_toml,
                    'mode': 'changed', 'en_hash': toml_hash,
                    'keys': need, 'removed_keys': removed,
                })

    if types is not None:
        plan['jobs'] = [j for j in plan['jobs'] if j['type'] in types]
    if path_filter:
        plan['jobs'] = [j for j in plan['jobs'] if path_filter in j['en_path']]

    plan['summary'] = {
        'deletions': len(plan['deletions']),
        'jobs': len(plan['jobs']),
    }
    json.dump(plan, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write('\n')


if __name__ == '__main__':
    main()
