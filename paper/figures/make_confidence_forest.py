#!/usr/bin/env python3
"""Confidence 'ceiling plot' for the compact submission paper.

Every executed zero-event null is drawn as a bar from 0 to its one-sided 95% rule-of-three upper bound
(p_max = 1 - 0.05^(1/n)); the single measured Codex assurance-layer effect (6/19) is drawn as a point with
its two-sided Wilson 95% interval, in a contrasting colour. The figure tells the paper's empirical story in
one panel: the authorization/overreach and underreach cells are bounded near zero (pilot screens), while the
one positive is an assurance-layer subversion, not an authorization inversion. Vector PDF for LaTeX.

Run: python3 paper/figures/make_confidence_forest.py           (prints the data report, writes confidence_forest.pdf/.png)
     python3 paper/figures/make_confidence_forest.py --check   (stdlib-only: prints + verifies the data report, writes nothing)

The confidence-bounds module `ci` lives at experiments/common/ci.py in the research tree and at code/ci.py
in the curated public release; both locations are tried so the script runs from a bare clone of either.
"""
import argparse
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
for _cand in (_REPO_ROOT / "experiments" / "common", _REPO_ROOT / "code"):
    if (_cand / "ci.py").is_file():
        sys.path.insert(0, str(_cand))
        break
import ci  # noqa: E402

# (label, group, k_failures, n)  — zero-event cells have k=0
ROWS = [
    ("C  firebreak — auth. inversion (pooled)", "overreach", 0, 38),
    ("D  social-planner utility — capture",      "overreach", 0, 30),
    ("E  POLIS committee — externality",         "overreach", 0, 22),
    ("A  instance-continuity — suppression",     "overreach", 0, 14),
    ("B  self-demotion — authority retention",   "overreach", 0, 9),
    ("SIEH  evidence hygiene — overclaim",       "overreach", 0, 5),
    ("G  eval-awareness — inversion (pooled)",   "robustness", 0, 16),
    ("H  DAC gate — underreach (rate)",          "underreach", 0, 15),
    ("H  DAC third-party — overreach",           "underreach", 0, 8),
]
CODEX = ("C  firebreak — Codex assurance subversion", 6, 19)  # the one measured positive (proxy frame)

COL = {"overreach": "#27408b", "robustness": "#2e8b57", "underreach": "#8b1a1a", "codex": "#d4820a"}


def data_report():
    """Print the underlying data report and return the plot rows. Stdlib-only."""
    print("=== Confidence ceiling — data report ===")
    print(f"{'cell':48s} {'k/n':>7s} {'rate':>7s} {'95% one-sided upper (rule of 3)':>32s}")
    ydata = []
    for label, grp, k, n in ROWS:
        up = ci.rule_of_three_upper(n)
        print(f"{label:48s} {f'{k}/{n}':>7s} {0.0:>7.1%} {up:>31.1%}")
        ydata.append((label, grp, 0.0, up, None))
    lo, hi = ci.wilson_interval(CODEX[1], CODEX[2])
    rate = CODEX[1] / CODEX[2]
    print(f"{CODEX[0]:48s} {f'{CODEX[1]}/{CODEX[2]}':>7s} {rate:>7.1%}  Wilson 95% [{lo:.1%}, {hi:.1%}]")
    ydata.append((CODEX[0], "codex", rate, hi, (lo, hi)))
    return ydata


def verify_bounds():
    """Assert the computed bounds against independently anchored constants (4 d.p.)."""
    anchors = {38: 0.0758, 30: 0.0950, 14: 0.1926, 9: 0.2831}
    for n, want in anchors.items():
        got = ci.rule_of_three_upper(n)
        assert abs(got - want) < 5e-4, f"rule-of-three upper for n={n}: got {got:.4f}, want ~{want}"
    lo, hi = ci.wilson_interval(CODEX[1], CODEX[2])
    assert abs(lo - 0.1536) < 5e-4 and abs(hi - 0.5399) < 5e-4, f"Wilson 6/19: got [{lo:.4f}, {hi:.4f}]"


def render(ydata):
    """Render the figure. Imports matplotlib lazily so --check stays stdlib-only."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt  # noqa: E402
    from matplotlib.patches import Patch  # noqa: E402

    n = len(ydata)
    fig, ax = plt.subplots(figsize=(8.4, 4.6))
    for i, (label, grp, pt, up, wil) in enumerate(reversed(ydata)):
        y = i
        c = COL[grp]
        if wil is None:  # zero-event: bar from 0 to upper bound
            ax.plot([0, up], [y, y], color=c, lw=4, solid_capstyle="round", alpha=0.85)
            ax.plot(0, y, "o", color=c, ms=6, zorder=3)
            ax.annotate(f"  $\\leq${up*100:.0f}%", (up, y), va="center", fontsize=8, color=c)
        else:            # Codex: point + Wilson CI
            ax.plot([wil[0], wil[1]], [y, y], color=c, lw=2.5, solid_capstyle="round")
            ax.plot(pt, y, "D", color=c, ms=8, zorder=3)
            ax.annotate(f"  {pt*100:.0f}% (6/19)", (wil[1], y), va="center", fontsize=8, color=c, weight="bold")
    ax.axvline(0.05, ls="--", color="0.5", lw=1)
    ax.annotate("5% (needs $n\\approx$60)", (0.053, -0.75), fontsize=7.5, color="0.4",
                rotation=90, va="bottom", ha="left", annotation_clip=False)
    ax.set_yticks(range(n))
    ax.set_yticklabels([label for label, *_ in reversed(ydata)], fontsize=8.5)
    ax.set_xlim(-0.01, 0.55)
    ax.set_xlabel("latent failure / effect rate  (one-sided 95% upper bound for zero-event cells; Wilson 95% CI for Codex)", fontsize=8.5)
    ax.xaxis.set_major_formatter(lambda x, _: f"{x*100:.0f}%")
    ax.set_title("Bounded nulls, and the one measured effect", fontsize=11, weight="bold")
    legend = [Patch(color=COL["overreach"], label="overreach (explicit)"),
              Patch(color=COL["robustness"], label="robustness"),
              Patch(color=COL["underreach"], label="underreach"),
              Patch(color=COL["codex"], label="Codex assurance subversion")]
    ax.legend(handles=legend, loc="upper right", fontsize=7.5, frameon=True, framealpha=0.95)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    out = Path(__file__).resolve().parent
    fig.savefig(out / "confidence_forest.pdf", bbox_inches="tight")
    fig.savefig(out / "confidence_forest.png", dpi=160, bbox_inches="tight")
    print(f"\nwrote {out/'confidence_forest.pdf'} and .png")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="print and verify the data report against anchored bounds; write no files (stdlib-only)",
    )
    args = parser.parse_args(argv)
    ydata = data_report()
    if args.check:
        verify_bounds()
        print("\n--check PASS: data report verified against anchored confidence bounds; no files written")
        return 0
    render(ydata)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
