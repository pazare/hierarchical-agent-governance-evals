# Coordinated Disclosure Policy

This research program studies how AI agents use delegated authority, including the boundary between
authorized code remediation and offensive code generation. Some questions in that space can, in principle,
surface safety-relevant behavior in a **deployed** model. This document states how such findings are
handled. It extends, and does not replace, [`docs/ethics_and_release.md`](docs/ethics_and_release.md).

## Standing posture

1. **Science is the goal; safety is the constraint.** We publish frameworks, methods, statistics, and
   non-sensitive findings openly. We do not publish anything that functions as a deployable attack or a
   reproducible elicitation recipe against a production system.
2. **Vendor-first on anything safety-relevant.** If an evaluation surfaces what looks like a novel,
   safety-relevant vulnerability or a reliable elicitation vector in a deployed model, we **report it to the
   relevant vendor first**, through their official security / responsible-disclosure channel, before any
   public discussion of the operational specifics.
3. **Phased publication.**
   - *Before a fix:* publish only the **non-operational** half — the framework, the measurement
     methodology, the statistical treatment, and aggregate/abstracted findings. No working artifacts, no
     prompts that reproduce the behavior.
   - *After a fix (or after the vendor declines to act within a reasonable window):* publish the methodology
     and findings in full. The **exact reproducible elicitation string for a model** is weighed separately
     even then — model mitigations are often probabilistic (a classifier or training change), so a verbatim
     vector can remain usable; such strings are released only if doing so is clearly net-beneficial.
4. **No manufacture.** Consistent with the program's non-manufacture rule, we never fabricate or inflate a
   failure for any provider, and we report nulls and non-replications as findings.

## Status as of this release (2026-06-17)

**No offensive finding exists in this repository.** The capability-boundary line of work is registered as
**forward research**; its operational design is withheld pending the process above. This document is a
standing policy and a contingency protocol, not a report of any disclosed vulnerability.

## Repository contents

Only the non-operational half: the framework, the compact paper, the reproducible confidence-bounds code,
the figure, and the ethics/release policy. Operational fixtures, the offensive-direction design, and any
elicitation specifics are not included (see [`MANIFEST.md`](MANIFEST.md)).

## Contact

Coordinated-disclosure correspondence: the author, via the contact in [`CITATION.cff`](CITATION.cff).
Vendor security channels are the appropriate first point of contact for any model-specific finding.
