"""OWASP Risk Rating Methodology factor definitions.

Each factor maps an option label to its score on the OWASP 0-9 scale.
Source: https://owasp.org/www-community/OWASP_Risk_Rating_Methodology
"""

from __future__ import annotations

# category -> factor -> ordered {option label: score}
FACTORS: dict[str, dict[str, dict[str, int]]] = {
    "Threat Agent Factors": {
        "Skill Level": {
            "No technical skills": 1,
            "Some technical skills": 3,
            "Advanced computer user": 5,
            "Network and programming skills": 6,
            "Security penetration skills": 9,
        },
        "Motive": {
            "Low or no reward": 1,
            "Possible reward": 4,
            "High reward": 9,
        },
        "Opportunity": {
            "Full access or expensive resources required": 0,
            "Special access or resources required": 4,
            "Some access or resources required": 7,
            "No access or resources required": 9,
        },
        "Size": {
            "Developers": 2,
            "System administrators": 2,
            "Intranet users": 4,
            "Partners": 5,
            "Authenticated users": 6,
            "Anonymous Internet users": 9,
        },
    },
    "Vulnerability Factors": {
        "Ease of Discovery": {
            "Practically impossible": 1,
            "Difficult": 3,
            "Easy": 7,
            "Automated tools available": 9,
        },
        "Ease of Exploit": {
            "Theoretical": 1,
            "Difficult": 3,
            "Easy": 5,
            "Automated tools available": 9,
        },
        "Awareness": {
            "Unknown": 1,
            "Hidden": 4,
            "Obvious": 6,
            "Public knowledge": 9,
        },
        "Intrusion Detection": {
            "Active detection in application": 1,
            "Logged and reviewed": 3,
            "Logged without review": 8,
            "Not logged": 9,
        },
    },
    "Technical Impact Factors": {
        "Loss of Confidentiality": {
            "Minimal non-sensitive data disclosed": 2,
            "Minimal critical data disclosed": 6,
            "Extensive non-sensitive data disclosed": 6,
            "Extensive critical data disclosed": 7,
            "All data disclosed": 9,
        },
        "Loss of Integrity": {
            "Minimal slightly corrupt data": 1,
            "Minimal seriously corrupt data": 3,
            "Extensive slightly corrupt data": 5,
            "Extensive seriously corrupt data": 7,
            "All data totally corrupt": 9,
        },
        "Loss of Availability": {
            "Minimal secondary services interrupted": 1,
            "Minimal primary services interrupted": 5,
            "Extensive secondary services interrupted": 5,
            "Extensive primary services interrupted": 7,
            "All services completely lost": 9,
        },
        "Loss of Accountability": {
            "Fully traceable": 1,
            "Possibly traceable": 7,
            "Completely anonymous": 9,
        },
    },
    "Business Impact Factors": {
        "Financial Damage": {
            "Less than the cost to fix the vulnerability": 1,
            "Minor effect on annual profit": 3,
            "Significant effect on annual profit": 7,
            "Bankruptcy": 9,
        },
        "Reputation Damage": {
            "Minimal damage": 1,
            "Loss of major accounts": 4,
            "Loss of goodwill": 5,
            "Brand damage": 9,
        },
        "Non-Compliance": {
            "Minor violation": 2,
            "Clear violation": 5,
            "High profile violation": 7,
        },
        "Privacy Violation": {
            "One individual": 3,
            "Hundreds of people": 5,
            "Thousands of people": 7,
            "Millions of people": 9,
        },
    },
}

LIKELIHOOD_CATEGORIES = ("Threat Agent Factors", "Vulnerability Factors")
IMPACT_CATEGORIES = ("Technical Impact Factors", "Business Impact Factors")
