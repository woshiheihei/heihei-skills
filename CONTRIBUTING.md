# Contributing

Thanks for helping improve this repository.

## Scope

This is a skill-first repository. The publishable skill under
`skills/x-thread-context-capture/` is the source of truth, and
`.agents/skills/` exists only as a repo-local discovery entry for Codex.

## Good contributions

- improve the skill workflow or prompt design
- refine selection rules, references, or templates
- improve validation, docs, or examples
- report reproducible bugs or edge cases

## Before opening a pull request

1. Keep changes focused and easy to review.
2. Preserve the default output contract:
   `./x-thread-contexts/x-thread-context-<author_handle>-<root_status_id>.md`
3. Avoid local machine paths, personal data, or machine-specific setup details.
4. Run the repository check:

```bash
python3 scripts/validate_skill_repo.py
```

## Editing expectations

- Put product and design documentation in `docs/`.
- Keep generated outputs in `x-thread-contexts/`.
- Keep the publishable skill in `skills/x-thread-context-capture/`.
- If you touch `.agents/skills/`, make sure it still resolves to the repository
  skill directory.
- Prefer concise, GitHub-friendly Markdown.

## Pull request guidance

- explain the user-facing reason for the change
- mention any workflow, output-format, or compatibility impact
- include before/after examples when changing output structure or selection
  rules
- keep commits intentional and descriptive
