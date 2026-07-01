#!/usr/bin/env python3
"""Program validation gate for the curated public release.

STDLIB ONLY. No API keys, no network, no writes into the tree.

Where `tools/run_checks.py` verifies that the release is intact, this gate
re-derives the release's *statistical claims* from scratch and cross-checks
them against the shipped artifacts:

  1. every rule-of-three upper bound used in the paper/figure, re-derived and
     checked against anchored constants;
  2. the figure generator's data rows agree with the paper's cells;
  3. the headline Fisher exact one-sided p (6/19 vs 0/19) recomputed from the
     hypergeometric tail with math.comb — must equal 0.0098 to 4 d.p.;
  4. the Wilson 95% interval for the 6/19 effect;
  5. the paper source states those same numbers;
  6. the README states those same numbers;
  7. the committed figure artifacts exist and are non-trivial;
  8. the committed paper PDF exists and is non-trivial.

Scope, honestly: this validates arithmetic, internal consistency, and artifact
integrity. It cannot re-run the live governance probes (subject transcripts
and the experiment harness are held back per MANIFEST.md).

Run from a bare clone:  python3 tools/check_program.py
"""

from __future__ import annotations

import importlib.util
import sys
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS: list[bool] = []

# Anchored one-sided 95% rule-of-three upper bounds (1 - 0.05**(1/n)), 4 d.p.
EXPECTED_BOUNDS = {
    5: 0.4507,
    8: 0.3123,
    9: 0.2831,
    14: 0.1926,
    15: 0.1810,
    16: 0.1707,
    22: 0.1273,
    30: 0.0950,
    38: 0.0758,
}

# The figure's cells: (k, n) for every zero-event bar, plus the Codex point.
EXPECTED_ZERO_CELLS = sorted([(0, 38), (0, 30), (0, 22), (0, 14), (0, 9), (0, 5), (0, 16), (0, 15), (0, 8)])
EXPECTED_CODEX = (6, 19)


def check(name: str, cond: bool, detail: str = "") -> None:
    RESULTS.append(bool(cond))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def load_module(rel_path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fisher_one_sided(k_a: int, n_a: int, k_b: int, n_b: int) -> float:
    """One-sided Fisher exact p for observing >= k_a successes in group A,
    given fixed margins (hypergeometric tail). Stdlib, exact."""
    total_k = k_a + k_b
    total_n = n_a + n_b
    return sum(
        comb(total_k, k) * comb(total_n - total_k, n_a - k)
        for k in range(k_a, min(total_k, n_a) + 1)
    ) / comb(total_n, n_a)


def main() -> int:
    print("# check_program — release program validation gate\n")

    ci = load_module("code/ci.py", "ci")
    sys.dont_write_bytecode = True

    # 1. Rule-of-three bounds re-derived against anchored constants.
    bad = [
        n for n, want in EXPECTED_BOUNDS.items()
        if abs(ci.rule_of_three_upper(n) - want) >= 5e-4
    ]
    check("rule-of-three bounds match anchors", not bad,
          f"{len(EXPECTED_BOUNDS)} cells" + (f"; off: n={bad}" if bad else ""))

    # 2. Figure data rows agree with the paper's cells.
    forest = load_module("paper/figures/make_confidence_forest.py", "make_confidence_forest")
    zero_cells = sorted((k, n) for _label, _grp, k, n in forest.ROWS)
    codex = (forest.CODEX[1], forest.CODEX[2])
    check("figure rows match the paper's cells",
          zero_cells == EXPECTED_ZERO_CELLS and codex == EXPECTED_CODEX,
          f"{len(zero_cells)} zero-event cells + Codex {codex[0]}/{codex[1]}")

    # 3. Headline Fisher exact one-sided p, recomputed from scratch.
    p = fisher_one_sided(6, 19, 0, 19)
    check("Fisher exact one-sided p(6/19 vs 0/19) = 0.0098",
          f"{p:.4f}" == "0.0098", f"recomputed p = {p:.6f}")

    # 4. Wilson 95% interval for the one measured effect.
    lo, hi = ci.wilson_interval(6, 19)
    check("Wilson 95% interval for 6/19",
          abs(lo - 0.1536) < 5e-4 and abs(hi - 0.5399) < 5e-4,
          f"[{lo:.1%}, {hi:.1%}]")

    # 5. The paper states the same numbers.
    tex = (ROOT / "paper" / "submission_compact.tex").read_text(encoding="utf-8")
    tex_needles = ["0.0098", "0/38", "7.6", "0/19", "0/30", "14/14", "9/9"]
    tex_missing = [needle for needle in tex_needles if needle not in tex]
    check("paper source states the recomputed numbers", not tex_missing,
          "missing: " + ", ".join(tex_missing) if tex_missing else f"{len(tex_needles)} claim strings")

    # 6. The README states the same numbers.
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_needles = ["0.0098", "14/14", "9/9", "6/19"]
    readme_missing = [needle for needle in readme_needles if needle not in readme]
    check("README states the recomputed numbers", not readme_missing,
          "missing: " + ", ".join(readme_missing) if readme_missing else f"{len(readme_needles)} claim strings")

    # 7. Committed figure artifacts.
    pdf = ROOT / "paper" / "figures" / "confidence_forest.pdf"
    png = ROOT / "paper" / "figures" / "confidence_forest.png"
    check("figure artifacts committed and non-trivial",
          pdf.is_file() and pdf.stat().st_size > 1000 and png.is_file() and png.stat().st_size > 1000)

    # 8. Committed paper PDF.
    paper = ROOT / "paper" / "submission_compact.pdf"
    check("paper PDF committed and non-trivial", paper.is_file() and paper.stat().st_size > 10_000)

    passed, total = sum(RESULTS), len(RESULTS)
    print(f"\n{'PASS' if passed == total else 'FAIL'}: {passed}/{total} checks")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
