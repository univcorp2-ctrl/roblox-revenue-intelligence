from revenue_intel.scoring import score_hypothesis


def test_ip_risk_is_penalized():
    safe = {"evidence": 1, "demand": 1, "distribution": 1, "automation": 1, "speed_to_revenue": 1, "ip_risk": 0}
    clone = dict(safe, ip_risk=1)
    assert score_hypothesis(safe) > score_hypothesis(clone)


def test_distribution_matters():
    direct = {"distribution": 1}
    hidden = {"distribution": 0}
    assert score_hypothesis(direct) > score_hypothesis(hidden)
