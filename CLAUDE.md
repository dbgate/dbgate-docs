# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository. It holds only agent-specific instructions — for project overview, setup, commands, architecture, and deployment, see [`README.md`](README.md). Keep common documentation there, not duplicated here; if a change here would make `README.md` stale, update `README.md` instead (or as well).

## Additional directories

`.claude/settings.json` grants read-only access to sibling repositories that are the source of knowledge for DbGate itself (write/edit is explicitly denied on all of them). Use them for context when writing or updating docs content (features, config options, terminology, changelog entries, etc.):

- `../dbgate` — main DbGate application source
- `../dbgate-merged` — merged/combined DbGate source variant
- `../dbgate-lite` — lite edition of DbGate (Solid.js, browser-based)
- `../web-dbgate-io` — dbgate.io marketing site source

When you need context from one of these projects, check its root `README.md` or `CLAUDE.md` first. Read further into the directory only when that isn't enough to answer the question (e.g. specific feature implementation or config option details).
