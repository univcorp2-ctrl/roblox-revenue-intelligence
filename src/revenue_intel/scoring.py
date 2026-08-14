from __future__ import annotations


def score_hypothesis(item: dict) -> float:
    """Commercial score: evidence and distribution dominate novelty."""
    evidence = float(item.get("evidence", 0))
    demand = float(item.get("demand", 0))
    distribution = float(item.get("distribution", 0))
    automation = float(item.get("automation", 0))
    speed = float(item.get("speed_to_revenue", 0))
    support = float(item.get("support_burden", 0))
    ip_risk = float(item.get("ip_risk", 0))
    platform_risk = float(item.get("platform_risk", 0))
    return (
        0.24 * evidence
        + 0.22 * demand
        + 0.20 * distribution
        + 0.16 * automation
        + 0.14 * speed
        - 0.10 * support
        - 0.18 * ip_risk
        - 0.18 * platform_risk
    )
