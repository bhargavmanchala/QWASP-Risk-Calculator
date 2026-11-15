"""Mitigation guidance shown for each overall severity."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Recommendation:
    banner: str
    kind: str  # Streamlit alert style: error | warning | info | success
    actions: tuple[str, ...]


RECOMMENDATIONS: dict[str, Recommendation] = {
    "Critical": Recommendation(
        "🚨 Critical risk! Act immediately.",
        "error",
        (
            "Treat as an incident: assemble a response team now",
            "Apply a compensating control or take the affected asset offline",
            "Fix and verify the vulnerability as the top priority",
            "Notify stakeholders and review compliance obligations",
        ),
    ),
    "High": Recommendation(
        "🚨 High risk detected. Immediate action required.",
        "warning",
        (
            "Conduct a comprehensive security assessment",
            "Implement urgent mitigation strategies",
            "Develop an incident response plan",
            "Allocate resources for remediation",
        ),
    ),
    "Medium": Recommendation(
        "⚠️ Moderate risk identified. Proactive measures needed.",
        "info",
        (
            "Perform a detailed vulnerability analysis",
            "Develop a targeted security improvement plan",
            "Prioritize critical vulnerabilities",
            "Enhance monitoring and detection mechanisms",
        ),
    ),
    "Low": Recommendation(
        "✅ Low risk. Maintain current security practices.",
        "success",
        (
            "Continue regular security assessments",
            "Maintain and update security controls",
            "Conduct periodic vulnerability scans",
        ),
    ),
    "Note": Recommendation(
        "ℹ️ Informational. No immediate action needed.",
        "success",
        (
            "Document the finding",
            "Re-evaluate if the system or threat landscape changes",
        ),
    ),
}
