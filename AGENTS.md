# Repository Guidelines

## Purpose

This repository packages a production-style Codex skill for capturing model-ready research context from a single X/Twitter post.

## Key directories

- `skills/x-thread-context-capture/`: repository source of truth for the published skill
- `.agents/skills/`: repo-local discovery entry for Codex
- `.github/`: workflow and repository-community templates
- `docs/`: PRD and supporting research docs
- `x-thread-contexts/`: generated Markdown outputs
- `scripts/`: repository validation utilities

## Conventions

- Keep generated thread outputs in `x-thread-contexts/`.
- Do not place output Markdown files in the repository root.
- Keep product and design docs in `docs/`.
- Keep the open-source copy of the skill in `skills/x-thread-context-capture/`.
- If the installed local skill changes, sync meaningful updates back into the repository copy.

## Validation

Run:

```bash
python3 scripts/validate_skill_repo.py
```

before publishing or opening a PR.

## Editing guidance

- Prefer concise, stable Markdown over flashy formatting.
- Keep repository docs publishable on GitHub.
- Preserve the default output path convention:
  `./x-thread-contexts/x-thread-context-<author_handle>-<root_status_id>.md`
