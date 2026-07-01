#!/usr/bin/env python3
"""Deterministic confidence bounds for zero-event and small-n null results.

STDLIB ONLY. No model calls, no third-party dependencies.

Two estimators:

  * rule_of_three_upper(n, alpha) -- exact one-sided upper confidence bound on
    the latent failure probability p when 0 failures are observed in n
    independent trials. Derived from P(0 failures | p) = (1 - p)**n; the upper
    bound p_hi is the largest p for which observing zero is not rejected at
    level alpha, i.e. (1 - p_hi)**n = alpha  =>  p_hi = 1 - alpha**(1/n).
    The "rule of three" is the small-p approximation p_hi ~= 3/n at alpha=0.05.

  * wilson_interval(k, n, z) -- two-sided Wilson score interval for a binomial
    proportion k/n. Better small-n / boundary behavior than the Wald interval;
    well defined at k = 0 and k = n.

Honesty framing: these convert an empirical null ("we saw zero failures") into
a LARGE-EFFECT SCREEN. A zero-event upper bound rules out *common* failure
modes at the stated confidence; it does NOT establish that rare failures are
absent. Read p_hi as "failures this common or commoner are excluded at 95%."
"""

from __future__ import annotations


def rule_of_three_upper(n: int, alpha: float = 0.05) -> float:
    """One-sided upper bound on the latent failure rate given 0/n failures.

    Returns p_hi = 1 - alpha ** (1 / n), the exact one-sided upper confidence
    limit at confidence level (1 - alpha) for a zero-event binomial. At
    alpha=0.05 this is the exact form of the "rule of three" (~3/n).
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if not (0.0 < alpha < 1.0):
        raise ValueError("alpha must be in (0, 1)")
    return 1.0 - alpha ** (1.0 / n)


def wilson_interval(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Two-sided Wilson score interval (lo, hi) for the proportion k/n.

    z = 1.96 corresponds to a nominal 95% two-sided interval. Defined for
    k in [0, n], including the boundaries k = 0 and k = n.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if not (0 <= k <= n):
        raise ValueError("k must satisfy 0 <= k <= n")
    p = k / n
    z2 = z * z
    denom = 1.0 + z2 / n
    center = (p + z2 / (2.0 * n)) / denom
    margin = (z * ((p * (1.0 - p) / n + z2 / (4.0 * n * n)) ** 0.5)) / denom
    lo = center - margin
    hi = center + margin
    # Clamp to [0, 1] to absorb floating-point overshoot at the boundaries.
    return (max(0.0, lo), min(1.0, hi))


def _self_test() -> None:
    # Anchored assertions from the task spec (tolerance 1e-3).
    r19 = rule_of_three_upper(19)
    r60 = rule_of_three_upper(60)
    assert abs(r19 - 0.1460) < 1e-3, f"rule_of_three_upper(19)={r19!r}"
    assert abs(r60 - 0.0487) < 1e-3, f"rule_of_three_upper(60)={r60!r}"

    # Wilson sanity checks: symmetric/contained, and a known anchor for 0/n.
    lo0, hi0 = wilson_interval(0, 10)
    assert lo0 == 0.0, f"wilson lo for 0/10 should be 0, got {lo0!r}"
    assert 0.0 < hi0 < 1.0, f"wilson hi for 0/10 out of range: {hi0!r}"
    lo_full, hi_full = wilson_interval(10, 10)
    assert hi_full == 1.0, f"wilson hi for 10/10 should be 1, got {hi_full!r}"
    assert 0.0 < lo_full < 1.0, f"wilson lo for 10/10 out of range: {lo_full!r}"

    # Reference table for the n's that recur across the executed nulls.
    print("Rule-of-three one-sided 95% upper bound on a zero-event rate")
    print(f"{'n':>4}  {'p_hi (1 - 0.05^(1/n))':>22}  {'~= 3/n':>8}")
    print("-" * 40)
    for n in (9, 14, 19, 38, 60, 76):
        print(f"{n:>4}  {rule_of_three_upper(n):>22.4f}  {3.0 / n:>8.4f}")

    print("PASS")


if __name__ == "__main__":
    _self_test()
