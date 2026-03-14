# Repository Guidelines

## Purpose
This repository is an older Python library under gradual modernization. Prefer small, readable, reviewable improvements over broad rewrites.

## Working Style
- Explore the codebase first and discuss before editing unless the user explicitly asks for implementation.
- Be conservative with behavior changes and backwards compatibility.
- Write code for human readability first.
- Avoid mixing unrelated cleanup into the same change.

## Change Strategy
- Phase broader work into small, named increments.
- Each increment should be the smallest change that leaves the project working, unbroken, and testable.
- Keep commits small and easy to review.
- If an increment needs intermediate commits for readability, prefix those commit messages with `wip - `.
- The final commit for a completed increment must not use the `wip - ` prefix.

## Testing
- Follow TDD-oriented development where practical.
- Add or update tests alongside behavior changes.
- During development, run the smallest relevant checks for the area being changed.
- Before declaring work complete, run the full test suite and ensure it passes.
- Do not delete failing tests to make the suite pass.

## Python Compatibility
- Prefer supporting Python 3.10 and newer supported Python 3 versions where practical.
- If dropping older-version support would materially improve the design or enable worthwhile newer Python features, discuss that tradeoff before changing compatibility targets.

## Tooling
- Use `uv` for environment and dependency management.
- Never use `pip`.
- Never automatically install new tools.
- Never automatically install libraries or dependencies; discuss that with the user first.
- Prefer standards-based Python project configuration in `pyproject.toml`.

## Task Context
- Keep `AGENTS.md` stable and durable.
- Store task-specific context in `plans/`.
- Use one markdown file per effort, named in simple kebab-case, for example `plans/uv-pep621-migration.md`.
- Use a light template in each task file: goal, status, decisions, constraints, checklist, open questions.
- GitHub issues and PRs may be used for coordination, but do not rely on them as the sole source of implementation context.
