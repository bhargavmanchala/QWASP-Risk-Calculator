"""OWASP Risk Rating calculator."""

from .scoring import RiskResult, calculate_risk

__all__ = ["RiskResult", "calculate_risk"]
