import pytest

from owasp_risk_calculator.factors import FACTORS
from owasp_risk_calculator.recommendations import RECOMMENDATIONS
from owasp_risk_calculator.scoring import (
    SEVERITY_MATRIX,
    calculate_risk,
    category_score,
    level_for,
)


def select(pick) -> dict[str, dict[str, str]]:
    """Build a selection by applying pick(options) -> label to every factor."""
    return {
        category: {factor: pick(options) for factor, options in factors.items()}
        for category, factors in FACTORS.items()
    }


def lowest(options):
    return min(options, key=options.get)


def highest(options):
    return max(options, key=options.get)


def test_all_scores_within_owasp_range():
    for factors in FACTORS.values():
        for options in factors.values():
            assert all(0 <= score <= 9 for score in options.values())


@pytest.mark.parametrize(
    ("score", "expected"),
    [(0, "Low"), (2.99, "Low"), (3, "Medium"), (5.99, "Medium"), (6, "High"), (9, "High")],
)
def test_level_boundaries(score, expected):
    assert level_for(score) == expected


def test_minimum_selection_is_note():
    result = calculate_risk(select(lowest))
    assert result.likelihood_level == "Low"
    assert result.impact_level == "Low"
    assert result.severity == "Note"


def test_maximum_selection_is_critical():
    result = calculate_risk(select(highest))
    assert result.likelihood_score == 9
    assert result.impact_score >= 6
    assert result.severity == "Critical"


def test_high_likelihood_low_impact_is_medium():
    selection = select(highest)
    for category in ("Technical Impact Factors", "Business Impact Factors"):
        selection[category] = {f: lowest(o) for f, o in FACTORS[category].items()}
    assert calculate_risk(selection).severity == "Medium"


def test_category_score_is_average():
    selection = select(lowest)
    selection["Threat Agent Factors"] = {
        "Skill Level": "Security penetration skills",  # 9
        "Motive": "Low or no reward",  # 1
        "Opportunity": "Full access or expensive resources required",  # 0
        "Size": "Anonymous Internet users",  # 9
    }
    assert category_score("Threat Agent Factors", selection) == pytest.approx(4.75)


def test_missing_factor_raises():
    selection = select(lowest)
    del selection["Vulnerability Factors"]["Awareness"]
    with pytest.raises(ValueError, match="Awareness"):
        calculate_risk(selection)


def test_unknown_option_raises():
    selection = select(lowest)
    selection["Threat Agent Factors"]["Motive"] = "Not a real option"
    with pytest.raises(ValueError, match="Unknown option"):
        calculate_risk(selection)


def test_every_severity_has_a_recommendation():
    assert set(SEVERITY_MATRIX.values()) <= set(RECOMMENDATIONS)
