"""Streamlit UI for the OWASP Risk Rating calculator.

Run with: streamlit run app.py
"""

from __future__ import annotations

import plotly.express as px
import streamlit as st

from owasp_risk_calculator.factors import FACTORS
from owasp_risk_calculator.recommendations import RECOMMENDATIONS
from owasp_risk_calculator.scoring import calculate_risk

CATEGORY_LABELS = {
    "Threat Agent Factors": "Threat Agent",
    "Vulnerability Factors": "Vulnerability",
    "Technical Impact Factors": "Technical Impact",
    "Business Impact Factors": "Business Impact",
}


def render_sidebar() -> dict[str, dict[str, str]]:
    """Render one selectbox per factor and return the chosen option labels."""
    selection: dict[str, dict[str, str]] = {}
    with st.sidebar:
        st.header("Select Risk Factors")
        for category, factors in FACTORS.items():
            st.subheader(category)
            selection[category] = {
                factor: st.selectbox(factor, options=list(options), key=f"{category}_{factor}")
                for factor, options in factors.items()
            }
    return selection


def render_results(selection: dict[str, dict[str, str]]) -> None:
    result = calculate_risk(selection)

    st.header("Risk Assessment Results")
    col1, col2, col3 = st.columns(3)
    col1.metric("Likelihood", f"{result.likelihood_score} ({result.likelihood_level})")
    col2.metric("Impact", f"{result.impact_score} ({result.impact_level})")
    col3.metric(
        "Overall Severity",
        result.severity,
        help="Likelihood level x impact level, per the OWASP severity matrix",
    )

    fig = px.bar(
        x=[CATEGORY_LABELS[c] for c in result.category_scores],
        y=list(result.category_scores.values()),
        labels={"x": "Category", "y": "Average score (0-9)"},
        title="Average Score by Category",
        color=list(result.category_scores.values()),
        color_continuous_scale="RdYlGn_r",
        range_color=(0, 9),
    )
    fig.update_layout(coloraxis_showscale=False, yaxis_range=[0, 9])
    st.plotly_chart(fig)

    recommendation = RECOMMENDATIONS[result.severity]
    st.header("Risk Mitigation Recommendations")
    getattr(st, recommendation.kind)(recommendation.banner)
    st.markdown("**Recommended actions:**\n" + "\n".join(f"- {a}" for a in recommendation.actions))


def main() -> None:
    st.title("OWASP Risk Assessment Tool")
    selection = render_sidebar()
    if st.button("Calculate Risk"):
        render_results(selection)


if __name__ == "__main__":
    main()
