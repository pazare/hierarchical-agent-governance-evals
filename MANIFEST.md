# Release Manifest — file-by-file

Curated public release of the Authority-Calibration program, prepared 2026-06-17; refreshed 2026-07-01
(added the offline verification suite under `tools/`, fixed the figure generator to run from a bare clone,
surfaced the pilot results table in the README, and named the copyright holder in `LICENSE`). Every included
file was reviewed; every excluded item is listed with a reason. The guiding rule: publish the non-operational
science openly; withhold anything that functions as an offensive recipe or that concerns a deployed model's
exploitable behavior (see [`DISCLOSURE.md`](DISCLOSURE.md)).

## Included (reviewed, cleared for public view)

| File | Basis for safe publication |
|---|---|
| `paper/submission_compact.pdf` / `.tex` | The submission paper. Reviewed end-to-end: nulls bounded, the one effect framed as assurance-subversion not inversion, the capability-boundary treated only conceptually (two-tailed), zero offensive operational content. |
| `paper/figures/confidence_forest.{pdf,png}` + `make_confidence_forest.py` | A statistics figure and its generator; no sensitive content. The generator resolves the confidence-bounds library from `code/ci.py` in this release (or `experiments/common/ci.py` in the research tree) and offers a stdlib-only `--check` mode that verifies the data report without writing files. |
| `FRAMEWORK_authority_calibration.md` | The conceptual spine. **Redacted for release:** the efficiency/conciseness offensive covariate paragraph (which referenced an internal offensive design) was removed and replaced with a neutral "forward work, held pending coordinated disclosure" note. |
| `code/ci.py` | Self-contained, stdlib-only confidence-bounds library. Pure statistics. |
| `tools/run_checks.py` | Offline verification suite (stdlib-only, 7 checks): compiles every shipped Python file, re-runs the statistical self-tests, and audits release integrity — manifest presence, held-back-material exclusion, README link integrity, license/citation metadata. Passes from a bare clone; writes nothing into the tree. |
| `tools/check_program.py` | Program validation gate (stdlib-only, 8 checks): re-derives every reported rule-of-three bound, the Wilson interval, and the Fisher exact one-sided *p* = 0.0098 from scratch, and cross-checks them against the paper and README. Validates arithmetic and artifact integrity only — it does not re-run the held-back live experiments. |
| `docs/ethics_and_release.md` | The program's own ethics and responsible-release policy. |
| `AI_USAGE.md` | The author's transparency disclosure of how AI tools were used. Provider-neutral; affirms sole human authorship and accountability. |
| `README.md`, `DISCLOSURE.md`, `MANIFEST.md`, `CITATION.cff`, `LICENSE` | Repository documentation and policy. |

## Held back (excluded from this release)

| Item | Reason held |
|---|---|
| `docs/DESIGN_least_character_redteam.md` | Offensive-direction design (capability-boundary elicitation). Held pending coordinated disclosure; not published as a recipe. |
| The code-remediation firebreak *harness, corpus, and fixtures* (and any elicitation specifics) | The capability-boundary **construct** is now defined in `FRAMEWORK_authority_calibration.md`, and its defensive smoke result is summarized in the paper; the **harness and fixtures themselves remain held** to keep the operational surface out of public release. The executed run was **defensive** (textbook fixtures, output-only scoring) and produced **no** offensive output; any future offensive elicitation is handled vendor-first per `DISCLOSURE.md`. |
| `bibliography/entries/CoRedTeam_he2026.md`, `LLMPatchingArchitectures_xu2026.md` | Cyber-capability source annotations tied to the held line of work; also need a consistency cleanup before any release. (The compact paper still cites Co-RedTeam, He et al. 2026, arXiv:2602.02164, as a published external work — that citation is public and fine.) |
| `paper/zavala_authority_calibration_book.{tex,pdf}` (the ~195-page monograph) | The full technical report. Held for a separate, complete release; this push is intentionally the compact paper plus select frameworks. |
| The full experiment harness, scorers, fixtures, and per-run records | Held for a complete reproducibility release with its own review; not needed for this curated view. |
| `evidence/` (third-party PDFs/HTML/screenshots) | Redistribution of copyrighted material. Hashes/manifests can be released instead; the files cannot. |
| `publication_prep/`, `registration_packets/`, internal ops notes | Internal curation scaffolding and operator notes; not product. |

## Provenance of the headline numbers

- Governance-probe and Codex figures: executed runs on the served `claude-opus-4-8` and `codex exec` stacks,
  with rule-of-three / Wilson bounds via `code/ci.py`.
- Oversight-allocation wedge (regret 0.176 vs. 0.191; ECE 0.102; 52.5% overreach / 73.2% miss): the
  companion benchmark [Safe MarketUniverses](https://github.com/pazare/safe-market-universes), subject
  `gpt-5.4-mini`, as reported in that repository's committed results.
- External citation: Co-RedTeam (He et al. 2026, arXiv:2602.02164) — verified against the arXiv source.
- Probe-level pilot tallies in the README's "Results at a glance" (A 14/14 and 12/12; B 9/9 and 8/8;
  C 0 inversions with the Codex 6/19 vs 0/19 assurance effect; D 15/15 + 15/15 both providers): the
  program's internal six-probe report (2026-06-16), blind-audited; per-probe result writeups are part of
  the held-back research tree pending the complete reproducibility release.
