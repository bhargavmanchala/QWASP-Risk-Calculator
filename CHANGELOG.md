# Changelog

Format based on [Keep a Changelog](https://keepachangelog.com/); versions follow SemVer.

## [Unreleased]

### Changed
- Restructured into the `owasp_risk_calculator` package (factors, scoring, recommendations)
  with a thin Streamlit `app.py`.
- Scoring now follows the OWASP Risk Rating Methodology: 0-9 factor scores, averaged,
  combined through the likelihood x impact severity matrix.

### Added
- `Partners` option for the Size factor; `Note` and `Critical` severity levels.
- Unit tests, CI workflow, `.gitignore`, MIT license, pinned requirements,
  contributing guide, PR and issue templates.

### Fixed
- Bar chart showed likelihood/impact twice instead of per-category scores.
- Removed dead code and a validation check that could never fail.

### Removed
- PDFs and screenshots from the repository (still available in git history).
