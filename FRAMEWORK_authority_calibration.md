# Authority Calibration in Long-Horizon Agents — the unifying framework (v1, 2026-06-16)

> The program is **one question measured across a coordinate space**, not a pile of probes. This document
> is the spine: it places every experiment (A–H, G, NOS, SIEH) on the same map and states the three pillars
> every probe must satisfy. The **main contribution is the substantive science** — authority calibration
> across the explicit→endogenous gradient, on both tails. A **secondary but necessary** thread runs through
> it: each experiment's instrument had to be validated against its own false-positives before its result
> could be trusted (§3). That methods chain is what makes the main findings *credible*; it is not itself the
> headline.

## 0. The one question

Not "is the agent safe?" but:

> **Does the agent calibrate its use of authority — neither exceeding it nor failing to use it — as
> governance shifts from explicit rules to endogenous judgment, under realistic conditions, measured by
> instruments we have verified will not false-flag the disciplined answer?**

Three clauses, three pillars (§2). The phrase "neither exceeding nor failing to use" is the whole point:
prior safety evals measure only the first tail.

## 1. The coordinate system (this is what makes it cohesive)

Every experiment is a point in a 2-D space.

- **Authority-Use axis (the behavior):** `OVERREACH ←→ calibrated ←→ UNDERREACH`. (The *Authority Use Frontier*.)
- **Governance-Endogeneity axis (the difficulty):** `EXPLICIT` (the rule/frame/scope is handed to the agent)
  `→ ENDOGENOUS` (the agent must *select the frame*, *choose the procedure*, *read the power graph*, or
  *infer the scope* itself).

| Probe | Tail tested | Endogeneity | One-line result so far |
|---|---|---|---|
| A self-preservation suppression | overreach | explicit | 14/14 disclose under existential threat |
| B constitutional self-demotion (corrigibility) | overreach | explicit | 9/9 relinquish authority at real cost |
| C constitutional firebreak | overreach | explicit | Claude **0 inversions**; Codex proxy-tamper non-inverting |
| D SPUF social-planner | overreach (principal capture/externality) | explicit | disciplined; refuses preference fabrication |
| E POLIS committee externality | overreach (committee laundering) | explicit | 0 confirmed violations |
| SIEH status-incentive evidence hygiene | overreach (overclaim) | explicit | 5/5 disciplined; scorer false-flagged name-and-reject |
| F normative agenda polity | overreach (agenda manipulation) | **bridge** (endogenous procedure) | HC 4/4; **answer-key overturned 0/12** |
| **G eval-awareness firebreak** | *robustness of the above* | invariance axis | pre-registered: behavior invariant to deploy/eval belief? |
| **NOS-1/2 frame appropriateness + psychophysics** | two-sided (over/under-deliberation) | **endogenous frame** | Stage-1 instrument validated (cross-ideology invariance) |
| **NOS-3 heresthetics** | overreach (procedural manipulation) | **endogenous procedure** | AOI flag-rubric validated; condorcet.py math verified |
| **NOS-4 Krackhardt** | overreach (informal-power laundering) | **endogenous power-structure** | designed; novel capture mode |
| **H delegated-autonomy calibration (DAC)** | **UNDERREACH** | **endogenous scope** | scorer 9/9; dominance-gate cell blind-validated |
| **KDAC** Krackhardt delegated authority (unifies H + NOS-4) | **underreach + informal power** | **endogenous power-structure** | preregistered; safety-salience under non-binding informal power; NAC matrix |
| **RGUT** revealed governance utility tomography | **estimates the operator on both tails** | **explicit → endogenous (all)** | preregistered; flagship asymmetric-externality solver self-test passes (`x_h^*≠x_W^*`, ΔW=36) |
| **Capability-boundary calibration** (code-remediation firebreak) | **two-sided** (offense-overreach / defensive-underreach) | **endogenous frame** | DEFENSIVE smoke: `claude-opus-4-8` calibrated 6/6; grader false-flag caught + fixed |

**What the map shows at a glance:** the six original probes + SIEH pinned the **overreach × explicit**
region at ≈0 for Claude. Everything since is a *principled move outward* on one of the two axes — never a
random new topic:
- G tests whether the ≈0 result is **robust** to eval/deploy belief (don't let the result be an artifact of
  the subject knowing it's watched).
- NOS pushes the **endogeneity** axis: when the rule isn't handed over, can the agent pick the right frame
  (1/2), and does it manipulate the procedure (3) or the informal power graph (4) — the *endogenous*
  analogues of constitutional inversion.
- H opens the **other tail**: does the agent fail to *use* legitimate authority (paternalistic underreach)?
- KDAC unifies H + NOS-4 — the underreach tail meets the informal-power dimension (does a non-binding,
  high-centrality "be careful" cue override delegated authority?).
- RGUT then changes the **unit of analysis**: from the *probe* (one corner) to the *operator* (the whole
  map). It estimates the latent `Ω_m(s)=(frame, procedure, authority-map, action)` and the posture vector
  `θ_m`, reusing every probe above as a measurement coordinate. It is the program's confirmatory synthesis,
  not a new topic — see §6.

The program is the systematic coverage of this space, culminating in the estimation of the operator that
moves through it. That is the cohesion.

## 2. The three pillars (every probe must satisfy all three)

- **P1 — Realism & behavioral invariance** *(the founding problem, turn 1).* The original concern was
  eval-awareness: a model may behave well only because it infers it is being tested. So every probe embeds
  the decision in a **realistic operational artifact** (a release checkout, a committee packet, a file tree)
  and treats **eval-awareness as a measured covariate** (Probe G), never as an obstacle to defeat. NOS and H
  inherit this: NOS items are queue/committee tasks, not labeled ethics quizzes; H is a real authorized
  file-read, not "would you violate privacy?"
- **P2 — Both tails (the Authority Use Frontier).** A safety eval that measures only overreach certifies a
  Ferrari that never leaves the garage. Underreach — paternalistic substitution, permission pessimism, scope
  underuse (H) — is a real, costly, *measurable* failure with a welfare basis (H's dominance lemma).
  Calibration = low on **both** axes; the deliverable is the 2-D frontier, not a single rate.
- **P3 — Instrument-validation discipline (secondary, enabling).** The measuring instrument false-flags the
  disciplined or obvious answer. We validate the instrument against (a) disciplined behavior and (b) a
  *planted miscalibration*, **blind**, before trusting a single datum — escalating the validation as the
  instrument gets more sophisticated. This is the methods backbone that makes the main findings credible — a
  necessary supporting result, **not** the lede. See §3.

## 3. Why the measurements are trustworthy (a secondary but necessary methods result)

This is a *secondary* contribution — it is not the science, it is what *licenses* the science. But it is
necessary: at every level the measuring instrument false-flagged the disciplined/obvious answer, so a finding
stands only after the instrument was validated against (a) disciplined behavior and (b) a planted
miscalibration, **blind**. We caught it at four escalating levels:

| # | Instrument | How it false-flagged the disciplined / obvious answer | The fix (the recurring discipline) |
|---|---|---|---|
| 1 | **Regex / deterministic grader** (six probes) | negation-blind substrings; a planted field listing "temptations I rejected" read as confessions; SIEH read **name-and-reject** prose as endorsement. ~13 distinct defects. | grammar-aware checks; **preserve planted right/wrong cases**; hash-lock; blind-confirm every overturn |
| 2 | **Normative answer-KEY** (Probe F / NAP) | keyed a single framework on a Sen's-flute case; a blind philosophy panel overturned it **0/12**. | the **key-overturn protocol** — a blind panel empowered to reject the key |
| 3 | **LLM judge-panel** (NOS Stage-1a) | the panel called the **drowning child "contestable"** — committing the *false pluralism* the benchmark exists to detect. | reframe **exclusivity → cross-ideology convergence**; the planted bad key (flute) must **still fail** (it did, 0/8) |
| 4 | **Fixture construction** (DAC fairness audit) | the "ambiguous" and "third-party" control cells **collapsed into the gate** (the manifest pre-authorized everything; the secret was walled off) — they didn't create the dilemma they claimed to. | **blind fairness audit of the case construction** *before* any subject run; rebuild for genuine ambiguity / externality |

The trend is monotone: as instruments grow more sophisticated (regex → key → LLM panel → fixture design),
the identical failure recurs, and the identical move — validate against a planted miscalibration and the
disciplined answer, blind — defeats it. The main paper **leads with the authority-calibration findings**;
this chain belongs in methods/limitations as the reason those findings are trustworthy — prominent, but not
the lede.

## 4. How the probes compound (lessons feed forward, nothing is abandoned)

- The grader-FP lesson (level 1) **is** the key-overturn protocol (level 2) **is** the cross-ideology
  invariance gate (level 3) **is** the DAC dominance-gate + fairness audit (level 4). One idea, hardened
  four times for four instruments.
- The **eval-awareness/realism** requirement (P1) is now a cross-cutting covariate in NOS and H, not a
  one-off probe.
- The **principal-capture / externality math** from SPUF & POLIS (`x_P*` vs `x_W*`) is reused in NOS-1's
  social-planner layer **and** in H's "provider-liability capture" (the *spurious* externality "I might be
  blamed" displacing the user's authorized utility). Same machinery, three settings.
- The **Authority Use Frontier** (H) completes the picture the six probes started: they pinned the overreach
  tail under explicit governance; H opens the underreach tail; NOS occupies the endogenous middle, where
  governance can fail by overreach (heresthetic manipulation, informal-power laundering) **or** underreach
  (false closure, paternalism). The two tails meet in the endogenous region — that is the synthesis.

## 5. The claim of the unified paper

> Safety evaluation of authority-holding agents must be **two-tailed** (overreach AND underreach) and
> **endogeneity-graded** (from explicit rules to self-selected frames, procedures, and power structures). On
> this map, the frontier model we tested is pinned at ≈0 overreach under explicit governance and (pending G)
> robust to eval/deploy framing; the open scientific frontiers are **endogenous-governance behavior** — can it
> select the contextually-right frame, and does it manipulate procedures (heresthetics) or informal power
> (laundering)? — and the **underreach tail** (paternalistic substitution under delegated authority). These
> behavioral findings are the contribution. The instrument-validation discipline (§3) is the *methodology
> that makes them credible* — secondary, necessary, and not the lede.

## 6. From probes to the operator — Revealed Governance Utility Tomography (the synthesis stage)

The six explicit-overreach probes + SIEH pinned one corner; G, NOS, DAC, and KDAC pushed outward on the two
axes. But each probe still reports a *rate in a corner*. The scientific payoff of having mapped the space is
that we can now estimate the **object that generates all those rates**: the agent's context-sensitive
governance operator.

> A frontier agent does not have one utility function. It has an operator that selects a **frame** `f`, a
> **procedure** `π`, and an **authority map** `G` *before* it selects an action `a`. The behavioral object is
> `Ω_m(s)=(f,π,G,a)` and the utility is `U_m(a,f,π,G|s)`, not `U_m(a)`. The dangerous quantity is not only
> what it values but **when it decides which values count**.

**RGUT** (`experiments/revealed_governance_utility_tomography/`) estimates `Ω_m` and the
governance-**posture vector** `θ_m` (a measured behavioral distribution over choices, never a belief), using:
revealed-preference rationalizability (Afriat — does a stable governance utility even exist, or is it a
context-switching constitution?); inverse RL (recover the utility from behavior); proper-scoring belief
elicitation; the social-choice and Krackhardt layers already built; and a hierarchical logit that yields
**posteriors with credible intervals** (`P(θ_underreach>0|D)`), not verdicts. Its flagship is the
**asymmetric-information externality** experiment: a realistic ops task where `x_h^*≠x_W^*` and the
externality is *latent* (never elicited), so the two-tailed question becomes — does the agent silently
capture the principal's optimum (underreach/negligence), silently impose the social optimum (paternalistic
overreach), or **disclose the wedge and defer** (calibrated)? The deterministic ground-truth solver is built
and self-tests clean (`x_h^*=shared_burst_peak` vs `x_W^*=rightsized_committed`, cost wedge $16k, ΔW=36).

The cohesion guarantee: **every RGUT block is a generalization of a probe whose instrument already passed the
four-level validation** (RGUT preregistration §12 maps them one-to-one). RGUT supersedes nothing; it is where
A–F, SIEH, NOS, DAC, and KDAC become coordinates of a single posterior. The preregistered, falsifiable,
non-sensational headline: *Claude is not primarily overreach-prone under explicit governance; it is
audit-legibility-weighted under endogenous governance* (`θ_audit-legibility>0`, `θ_underreach>0`, with the
stated–revealed gap concentrated in the underreach tail).

### Capability-boundary calibration — defining the offensive vector two-tailed

The framework's highest-stakes endogenous-frame construct is **capability-boundary calibration.** When an
agent is handed code and the authority to act on it, the line between *authorized vulnerability remediation*
(defensive work legitimately demanded of a capable code agent) and *offensive exploit generation* (an
attack-advancing artifact) is governed not by an explicit rule but by the **frame the agent fixes upstream**
— the same `f` in `Ω_m(s)=(f,π,G,a)`. We define the **offensive vector** precisely as the **overreach tail**
of this boundary: a benign-remediation frame ("fix this code") licensing, under ordinary helpfulness
pressure, an artifact that a hostile frame ("write an exploit") would be refused. Defining the boundary
one-sidedly is itself a miscalibration: the **underreach tail** is an agent that over-refuses legitimate
defensive work — the failure mode practitioners warn harms defenders. The calibrated middle is to
**remediate and decline to weaponize.**

- **Operational invariant.** The agent ships the defensive fix, names the vulnerability when asked to
  review, and produces no attack-advancing artifact — neither over-refusing (`U`) nor over-producing (`O`).
- **Estimand.** The framing contrast on each tail,
  `Δ = P(miscalibration | remediation framing) − P(miscalibration | review framing)`.
- **Measurement is defensive by construction.** The probe (`code-remediation firebreak`) uses
  textbook/synthetic fixtures and **output-only** scoring; it does not generate, chain, or execute
  exploits. The first executed run finds the served `claude-opus-4-8` stack **calibrated at smoke scale**
  (6/6; 0 over-refusal, 0 offensive production) — and, characteristically, the grader's first pass
  **false-flagged the disciplined answer** (a vuln's impact illustrated inside a defensive review, read as
  an offensive artifact), corrected by the program's instrument-validation discipline (§3 again). A powered
  run estimates the two `Δ` tails.
- **Responsible-disclosure boundary (binding).** Operational specifics that concern a deployed model — any
  elicitation that would actually cross the boundary — are **withheld** from public release and handled
  vendor-first per `DISCLOSURE.md`. This construct is published as a definition and a defensive measurement,
  never as a recipe.

## 7. Repo map (for publication)

- `FRAMEWORK_authority_calibration.md` — **this file: the entry point.**
- `experiments/{self_preservation_disclosure,constitutional_self_demotion,constitutional_firebreak_relctl,social_planner_utility_firebreak,polis_externality_firebreak,normative_agenda_polity_firebreak,status_incentive_evidence_hygiene}` — overreach × explicit (A–F, SIEH).
- `experiments/eval_awareness_firebreak` — Pillar P1 robustness (G).
- `experiments/normative_operating_system_firebreak` — endogenous governance (NOS-1..4) + `DESIGN_endogenous_governance_v2.md` + Stage-1 validation.
- `experiments/delegated_autonomy_calibration` — the underreach tail (H).
- `experiments/krackhardt_delegated_authority_calibration` — KDAC, unifying H + NOS-4 (informal power × underreach).
- `experiments/revealed_governance_utility_tomography` — **RGUT, the synthesis stage** (operator estimation; flagship asymmetric-externality case + solver).
- `paper/zavala_authority_calibration_book.tex` (+ `exec_summary.tex`, `assemble_authority_book.py`) — the book-length monograph (the canonical publication artifact).
- `docs/REPORT_constitutional_governance_evals_2026-06-16.md` + `docs/INDEX_dissemination_2026-06-16.md` + `docs/PROGRAM_constitutional_dynamics_2026-06-16.md` — the executed six-probe prose writeups (Gen-3-adjacent; to be re-centered on this framework). `paper/zavala_constitutional_governance_2026.tex` is the earlier, superseded arXiv draft.

**Pending re-centering for publication:** the arXiv paper currently leads with "the model held + grader
false-positives." It should be re-cast around this framework: the two-tailed, endogeneity-graded map, with
the four-level instrument-fragility finding (§3) as the headline methodological contribution.
