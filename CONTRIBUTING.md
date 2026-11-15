# Contributing

## Setup
```bash
python -m venv .venv
.venv/Scripts/activate        # Windows (Linux/macOS: source .venv/bin/activate)
pip install -r requirements-dev.txt
```

## Workflow
1. Branch from `main`: `feat/…`, `fix/…`, `docs/…`, `refactor/…`, `chore/…`.
2. Make small, focused commits using [Conventional Commits](https://www.conventionalcommits.org/)
   (`feat: add partners option`, `fix: correct severity boundary`).
3. Before pushing run:
   ```bash
   ruff check . && ruff format --check . && pytest
   ```
4. Open a pull request using the template. CI must pass; squash-merge into `main`.

## Rules
- Never commit directly to `main`.
- Never commit secrets, `.env` files or large binaries (screenshots/PDFs go in release
  assets or the wiki, not the repo).
- Scoring changes must keep to the
  [OWASP Risk Rating Methodology](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)
  and come with tests.
