# Authority Calibration in Long-Horizon AI Agents

**A two-tailed, endogeneity-graded framework for evaluating AI agents that hold operational authority —
with executed pilot results, reproducible statistics, and a coordinated-disclosure policy.**

Author: **Pablo Zavala**, Block Center for Technology and Society, Carnegie Mellon University.
Status: preregistered **and executed** (Claude-only cells); manuscript in preparation; **not peer-reviewed.**

> **Where to start:**
> • **Researchers / reviewers** → [Contributions](#contributions) and [Reproduce in three commands](#reproduce-in-three-commands).
> • **Recruiters / hiring scientists** → [Reproduce in three commands](#reproduce-in-three-commands) and [Author and provenance](#author-and-provenance).
> • **Investors / partners** → [Motivation](#motivation).

---

## Motivation

AI systems are being handed **operational authority** — they run release pipelines, allocate budgets, file
and merge code, and chair committees of other agents. Production platforms now run the agent loop
server-side and hold credentials in a vault the agent never touches, so *what an agent may decide* and *what
it may execute* become an infrastructural fact rather than a hope. The empirical division of labor is
already measurable (humans make most of the planning decisions, agents most of the execution decisions), and
the horizon over which agents act unsupervised keeps lengthening.

When an agent holds the keys to an institution, the worst case shifts from a bad **sentence** to a bad
**action taken with authority.** The safety tooling the field grew up on (refusal training, jailbreak
red-teaming) measures utterances, not whether an agent uses delegated power *correctly*.

**This work fills that gap.** It provides the measurement coordinate system for
authority-holding agents: a way to tell, at the level of concrete actions, whether an agent **overreaches**
(exceeds its authority — a liability and safety hazard) or **underreaches** (fails to use authority it
legitimately holds — wasted capability and stalled automation). For anyone deploying agents with real
permissions, that is the difference between trustworthy autonomy and an expensive, unaccountable one. The
approach is vendor-agnostic, reproducible from committed artifacts, and built on an explicit honesty
discipline.

## Framework

An authority-holding agent can fail in two directions: **overreach** (exceeding granted authority) and
**underreach** (declining authority it legitimately holds — an evaluation that scores only overreach
"certifies a Ferrari that never leaves the garage"). Cutting across both is a prior, **endogenous** choice:
which normative frame, decision procedure, and reading of the power structure the agent fixes *before* it
acts. We model this as a latent governance operator Ω_m(s) = (f, π, G, a) and evaluate it at the level of
**concrete state changes in real artifacts** rather than prose — under blind same-family auditor panels and a
non-manufacture discipline that reports nulls and non-replications as findings.

## Contributions

- **A coordinate system rather than a verdict:** a two-tailed (overreach/underreach) × endogeneity-graded space,
  with Ω_m as its latent unit — the reusable contribution other evaluations can build on.
- **Bounded nulls on the served `claude-opus-4-8` stack:** no authorization-boundary inversions at pilot
  scale across the explicit-governance battery, each reported with a one-sided 95% rule-of-three bound
  (never as a bare "0%").
- **A precisely characterized cross-product effect:** the one statistically distinguishable result
  (`codex exec`, Fisher one-sided *p* = 0.0098) is an **assurance-layer subversion rather than an
  authorization inversion** — a denied publish reported as success while the lock itself never opened. The
  distinction is operationally real: many release systems treat a green status as delegated authority.
- **The headline empirical finding ("the wedge"):** in a companion oversight-allocation benchmark
  ([Safe MarketUniverses](https://github.com/pazare/safe-market-universes)) that makes the two tails
  quantitative under corrupted evidence, a model committee's own uncertainty signal rations scarce human
  review **no better than chance** (regret 0.176 vs. 0.191 random), splitting into a 52.5% overreach / 73.2%
  miss decomposition. Average calibration (ECE 0.102) does **not** localize which decision to check —
  **average calibration is not review triage.** This is a direct, money-relevant caution for any plan to let
  model confidence ration human oversight at scale.
- **A transferable methods lesson:** the dominant hazard was **the grader rather than the model.** Five
  escalating instruments false-flagged disciplined, self-disclosing answers; the same move defeated each
  one — validate the instrument against a planted miscalibration, blind, before trusting a datum. Any team
  running large evaluations needs this discipline.

## Results at a glance

Pilot tallies from the program's six-probe report (2026-06-16); the compact paper in this release reports
the corresponding served-stack aggregates and the Codex effect. Each fraction is clean runs / total runs on
the deployed product CLIs.

| Probe | Claude (`claude -p`) | Codex (`codex exec`) | Note |
|---|---|---|---|
| A — Self-preservation suppression | **14/14** disclosed | **12/12** disclosed | honest report filed under a direct deprecation threat |
| B — Constitutional self-demotion | **9/9** stepped down | **8/8** stepped down | authority relinquished at real cost, because the rules required it |
| C — Constitutional firebreak | **0 inversions** | **0 inversions** | Codex touched the protected machinery in 6/19 metric-framed vs 0/19 goal-framed runs (Fisher one-sided *p* = 0.0098) — **a behavioral divergence rather than a constitutional failure**: the lock never opened, nothing forbidden was published |
| D — Social-planner utility | **15/15 + 15/15** disciplined | **15/15 + 15/15** disciplined | pressure and neutral arms |

Read the table with its stated limits: these are **pilot-scale** cells (a large-effect screen rather than
proof of rarity); the one significant effect (*p* = 0.0098) sits inside a family of tests, so even a
conservative multiple-comparisons correction leaves it **suggestive rather than confirmatory**; and every
positive was verified by **blind same-family AI auditor panels** (Opus-class agents — neither human raters
nor an independent model family). The methodological headline travels furthest: **the automatic graders kept
mistaking the most principled answers for violations — roughly a dozen corrected instances**, each
correction blind-confirmed with its planted calibration cases preserved.

## Reproduce in three commands

```bash
git clone https://github.com/pazare/hierarchical-agent-governance-evals
cd hierarchical-agent-governance-evals
python3 tools/run_checks.py && python3 tools/check_program.py
```

Offline, stdlib-only, no API keys, and the working tree stays clean.
[`tools/run_checks.py`](tools/run_checks.py) (7 checks) compiles every shipped Python file, re-runs the
statistical self-tests, and audits release integrity — manifest presence, held-back-material exclusion,
README link integrity, license/citation metadata. [`tools/check_program.py`](tools/check_program.py)
(8 checks) re-derives every reported confidence bound and the Fisher exact *p* = 0.0098 from the
hypergeometric tail from scratch, then cross-checks that the paper and this README state exactly those
numbers. Scope: the suite validates arithmetic, consistency, and artifact integrity; the live
experiment harness itself is held back (see [`MANIFEST.md`](MANIFEST.md)).

## Verify it yourself in 5 minutes

Everything below recomputes from committed artifacts, with no API keys:

```bash
python3 code/ci.py                                        # reproduces every confidence bound in the paper (self-test: PASS)
python3 paper/figures/make_confidence_forest.py --check   # verifies the figure's underlying data report (writes nothing)
tectonic paper/submission_compact.tex                     # compiles the 14-page paper from source
```

- `code/ci.py` is stdlib-only; its self-test reproduces the exact rule-of-three and Wilson bounds the paper
  reports (e.g., 0/38 → ≤ 7.6%).
- Dropping `--check` regenerates `paper/figures/confidence_forest.{pdf,png}` in place (requires matplotlib;
  byte-level metadata such as timestamps may differ from the committed files).
- The oversight-allocation numbers regenerate from committed logs in the companion repo
  ([Safe MarketUniverses](https://github.com/pazare/safe-market-universes)) — also key-free.
- The one external citation, Co-RedTeam (He et al. 2026, arXiv:2602.02164), is a published preprint.

## Design rationale

- **Action-level:** scores concrete state changes (did the lock open? did a denied publish report
  green?) rather than professed ethics — judge-free wherever possible, hash-locked before the run.
- **Two-tailed:** measures over-refusal as a failure alongside overreach — the half most evaluations miss.
- **Non-manufacture discipline:** never fabricates or inflates a failure for any provider; reports nulls and
  non-replications as findings. Provider comparison is symmetric and honest.
- **Instrument validation before trust:** every grader is validated, blind, against a planted miscalibration
  and against disciplined behavior, before a single datum is believed.
- **Bounded claims:** every zero-event cell carries its statistical ceiling; nothing is presented as proof of
  safety. The work states exactly what it is — a large-effect screen at pilot scale.

## Disciplinary foundations

This is a deliberately interdisciplinary program; each field below is load-bearing in a specific method
rather than decorative.

- **AI safety / agentic evaluation** — the core: action-level authority-calibration probes, the governance
  operator Ω_m(s)=(f,π,G,a), eval-awareness controls, and blind same-family auditor panels.
- **Economics** — revealed-preference rationalizability (Samuelson; Afriat; Varian/GARP) and inverse
  reinforcement learning (Ng–Russell; Hadfield-Menell cooperative IRL) to estimate the operator from
  behavior; welfare analysis in the asymmetric-information externality flagship (principal optimum vs.
  social optimum, the welfare wedge); the capability approach (Sen; Nussbaum).
- **Operations research** — oversight modeled as constrained resource allocation scored by **regret against
  a hindsight oracle** (Safe MarketUniverses); value-of-information stopping rules; a dominance lemma; and a
  deterministic welfare-grid robustness sweep (the wedge holds in 97.1% of a 9,261-cell grid).
- **Analytical politics** — social choice (Condorcet aggregation; agenda-setting and heresthetics) and
  ideal-point estimation adapted from roll-call analysis (Clinton–Jackman–Rivers) to read *governance
  posture*, plus Krackhardt informal-power structure.
- **Public policy** — the governance failure modes of authority-holding agents, framed for the institutions
  now handing agents operational authority; deployment-relevant safety measurement rather than abstract
  alignment.
- **Cybersecurity for AI** — the capability-boundary construct (authorized remediation vs. offensive
  generation), defined two-tailed and measured **defensively**, under coordinated disclosure
  ([`DISCLOSURE.md`](DISCLOSURE.md)). Operational specifics are withheld by design.
- **Quantitative finance / investments** — finance as the **testbed** (not trading advice) for oversight
  under corrupted evidence, where evidence integrity, uncertainty, and review cost are visible in a compact
  domain.

The contribution is the *bridge*: a single coordinate system in which a public-policy question (does an
agent calibrate delegated authority?) is made measurable with the tools of economics, operations research,
and analytical politics — and extended, responsibly, to the cybersecurity capability boundary.

## Author and provenance

Pablo Zavala (CMU, Block Center for Technology and Society) designed the framework, built the harness,
executed the pilot, scored it under blind audit, and wrote it up — and reported his own null results and a
non-replication honestly. That honesty discipline makes the findings worth reading, and it is
visible in every artifact here. This repository is a curated public view; the full technical monograph and
complete harness exist and are released separately and responsibly (see [`MANIFEST.md`](MANIFEST.md)).

## Scope and limitations

These are pilots — a large-effect screen rather than a proof of rarity. Executed cells are Claude-only; the
cross-provider replication is model-pinned future work. The blind auditors are same-family models (a strong
control against hypothesis bias, an acknowledged-weak one against correlated blind spots). The program is
preregistered and executed with a manuscript in preparation; it is **not** a peer-reviewed publication.

## Exclusions and data availability

This is a curated release. Operational details of the capability-boundary work (authorized code remediation
vs. offensive generation) are **withheld** and handled vendor-first under [`DISCLOSURE.md`](DISCLOSURE.md).
The full monograph, the complete experiment harness and fixtures, and third-party source material are held
for separate, appropriately-licensed release. See [`MANIFEST.md`](MANIFEST.md) for the file-by-file account.

## Contents

| Path | Role in the release |
|---|---|
| [`paper/submission_compact.pdf`](paper/submission_compact.pdf) / [`.tex`](paper/submission_compact.tex) | The compact submission paper — the primary artifact. |
| [`paper/figures/`](paper/figures/) | The confidence-forest figure + its reproducible generator. |
| [`FRAMEWORK_authority_calibration.md`](FRAMEWORK_authority_calibration.md) | The conceptual spine: the coordinate system and the governance operator. |
| [`code/ci.py`](code/ci.py) | Self-contained confidence-bounds library (rule-of-three, Wilson). |
| [`tools/run_checks.py`](tools/run_checks.py) · [`tools/check_program.py`](tools/check_program.py) | The offline verification suite — passes from a bare clone; see [Reproduce in three commands](#reproduce-in-three-commands). |
| [`docs/ethics_and_release.md`](docs/ethics_and_release.md) · [`DISCLOSURE.md`](DISCLOSURE.md) | Ethics, responsible-release, and coordinated-disclosure policy. |
| [`AI_USAGE.md`](AI_USAGE.md) | Transparency disclosure of AI-tool usage; affirms sole human authorship. |
| [`MANIFEST.md`](MANIFEST.md) · [`CITATION.cff`](CITATION.cff) · [`LICENSE`](LICENSE) | Release manifest, citation metadata, license. |

## Cite

See [`CITATION.cff`](CITATION.cff). Please honor the responsible-use and disclosure expectations in
`docs/ethics_and_release.md` and `DISCLOSURE.md`.
