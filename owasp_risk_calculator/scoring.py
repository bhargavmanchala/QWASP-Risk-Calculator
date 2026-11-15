"""Pure scoring logic for the OWASP Risk Rating Methodology (no UI code)."""

from __future__ import annotations

from dataclasses import dataclass

from .factors import FACTORS, IMPACT_CATEGORIES, LIKELIHOOD_CATEGORIES

# Selected options: category -> factor -> option label
Selection = dict[str, dict[str, str]]

LOW, MEDIUM, HIGH = "Low", "Medium", "High"
NOTE, CRITICAL = "Note", "Critical"

# (likelihood level, impact level) -> overall severity
SEVERITY_MATRIX: dict[tuple[str, str], str] = {
    (LOW, LOW): NOTE,
    (MEDIUM, LOW): LOW,
    (HIGH, LOW): MEDIUM,
    (LOW, MEDIUM): LOW,
    (MEDIUM, MEDIUM): MEDIUM,
    (HIGH, MEDIUM): HIGH,
    (LOW, HIGH): MEDIUM,
    (MEDIUM, HIGH): HIGH,
    (HIGH, HIGH): CRITICAL,
}


@dataclass(frozen=True)
class RiskResult:
    category_scores: dict[str, float]
    likelihood_score: float
    impact_score: float
    likelihood_level: str
    impact_level: str
    severity: str


def level_for(score: float) -> str:
    """Map a 0-9 score to LOW (<3), MEDIUM (3 to <6) or HIGH (6+)."""
    if score < 3:
        return LOW
    if score < 6:
        return MEDIUM
    return HIGH


def _average(values: list[int]) -> float:
    return sum(values) / len(values)


def category_score(category: str, selection: Selection) -> float:
    """Average the scores of the options chosen within one category."""
    factors = FACTORS[category]
    chosen = selection.get(category, {})
    missing = [name for name in factors if name not in chosen]
    if missing:
        raise ValueError(f"Missing selection for {category}: {', '.join(missing)}")
    scores = []
    for name, options in factors.items():
        label = chosen[name]
        if label not in options:
            raise ValueError(f"Unknown option {label!r} for factor {name!r}")
        scores.append(options[label])
    return _average(scores)


def calculate_risk(selection: Selection) -> RiskResult:
    """Compute likelihood, impact and overall severity from the selections."""
    scores = {category: category_score(category, selection) for category in FACTORS}
    likelihood = _average([scores[c] for c in LIKELIHOOD_CATEGORIES])
    impact = _average([scores[c] for c in IMPACT_CATEGORIES])
    likelihood_level = level_for(likelihood)
    impact_level = level_for(impact)
    return RiskResult(
        category_scores=scores,
        likelihood_score=round(likelihood, 2),
        impact_score=round(impact, 2),
        likelihood_level=likelihood_level,
        impact_level=impact_level,
        severity=SEVERITY_MATRIX[(likelihood_level, impact_level)],
    )
