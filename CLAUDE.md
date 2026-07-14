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
