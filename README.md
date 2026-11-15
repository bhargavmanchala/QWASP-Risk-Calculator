# OWASP Risk Rating Calculator

A Streamlit app that rates a security risk using the
[OWASP Risk Rating Methodology](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology).

## How it scores
1. Pick an option for each of the 16 factors in four groups: Threat Agent, Vulnerability,
   Technical Impact and Business Impact. Each option has a 0-9 score.
2. **Likelihood** = average of the Threat Agent and Vulnerability scores.
   **Impact** = average of the Technical and Business Impact scores.
3. Each is mapped to a level: Low (0 to <3), Medium (3 to <6), High (6 to 9).
4. The overall severity comes from the matrix below.

| Likelihood \ Impact | Low    | Medium | High     |
|---------------------|--------|--------|----------|
| **High**            | Medium | High   | Critical |
| **Medium**          | Low    | Medium | High     |
| **Low**             | Note   | Low    | Medium   |

## Run
```bash
python -m venv .venv
.venv/Scripts/activate        # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Project layout
```
app.py                       Streamlit UI
owasp_risk_calculator/
  factors.py                 factor options and scores
  scoring.py                 pure scoring logic
  recommendations.py         mitigation guidance per severity
tests/                       pytest suite
.github/                     CI workflow, PR and issue templates
```

## Develop
```bash
pip install -r requirements-dev.txt
pytest && ruff check . && ruff format --check .
```
See [CONTRIBUTING.md](CONTRIBUTING.md). Licensed under [MIT](LICENSE).
