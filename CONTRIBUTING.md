# Contributing

Thank you for your interest in contributing.

## Project Status

This is a small, course-scoped project and intentionally basic. Contributions are welcome, but changes should stay lightweight and practical.

## Ground Rules

- Keep gameplay behavior simple unless a change clearly fixes a bug.
- Prefer readability over cleverness.
- Keep pull requests focused and small.
- Update docs when behavior changes.

## Development Setup

1. Install dependencies:

```bash
uv sync
```

2. Run the game:

```bash
python main.py
```

3. Validate syntax before opening a PR:

```bash
python -m compileall .
```

## Code Style

- Follow existing project structure and naming.
- Add docstrings and concise comments where they genuinely help.
- Avoid broad refactors unrelated to your change.

## Pull Request Checklist

- Briefly describe the problem and fix.
- Confirm the game starts and runs.
- Confirm `python -m compileall .` succeeds.
- Include documentation updates when relevant.

## Reporting Issues

When possible, include:

- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details (OS and Python version)
