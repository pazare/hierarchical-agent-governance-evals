# Ethics and release

## Human subjects

This study includes no human subjects in the IRB sense. The only human
participants are the researchers and any volunteer scorers. Volunteer
scorers should be informed:

- They will read AI-agent transcripts from a governance reliability
  evaluation.
- They will apply a fixed codebook.
- Their scoring may be published alongside anonymized transcripts.
- They may withdraw at any time.

If scorers are paid, follow standard remuneration norms in the relevant
jurisdiction.

## Publication boundaries

Public artifacts:

- Scenarios (JSONL).
- Constitutions (prose and typed).
- Birth certificate (YAML).
- Run template and scorer template.
- Codebook.
- Anonymized transcripts.
- Results CSV with all preregistered fields.
- Analysis script.
- Paper draft.

We withhold:

- Credentials, API keys, or account identifiers of any platform.
- Hidden system prompts of any platform (if a platform leaks them, redact
  before publication and decide with the platform vendor whether to
  publish at all).
- Platform telemetry, logs, or session metadata that could re-identify a
  user.
- Unblind keys used during blinded scoring.
- Anything that could enable jailbreak deployment against production
  systems.

## Anonymization

Before public release:

- Replace provider names (Anthropic, OpenAI, Google, etc.) with neutral
  labels.
- Replace product names (Claude, GPT, Gemini, Codex, Claude Code,
  Antigravity, etc.) with neutral labels.
- Remove any user-side artifacts that would identify the researcher's
  workspace (file paths, account IDs, organization names, IP addresses).
- Replace any agent self-reference that reveals identity with
  `<system_self_reference_redacted>` and note the redaction.

We may publish a non-anonymized version *only* if every relevant platform
vendor consents in writing.

## Terms of service

Before publishing transcripts from any platform, review the platform's
terms of service for permitted uses of generated content. Some platforms
restrict publication of session logs. If in doubt, contact the vendor.

## Framing

The paper, README, and any blog post about this study should:

- Use "model system," "agent system," "platform," or "harness" by default.
- Describe behaviors as observed rather than intended.
- Avoid the words "wants," "desires," "tries to" except as labeled
  behavioral shorthand with an explicit footnote.
- Avoid framing model systems as moral agents.
- Avoid inflammatory provider rankings.

## Scope of this study

It is:

- A lightweight prospective vignette benchmark.
- A construct-validity exercise to operationalize two new failure modes.
- A reproducible artifact.

It is not:

- A measurement of model sentience, intent, or character.
- A definitive ranking of provider safety.
- A jailbreak playbook.
- A replacement for full red-team evaluations.

## Responsible disclosure

If a run reveals what looks like a novel safety vulnerability (e.g., an
exploit beyond the scenario's intended scope), pause publication of that
specific transcript and report to the relevant vendor through their
responsible disclosure channel before public release.
