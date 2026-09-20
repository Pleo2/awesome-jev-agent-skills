---
name: jev-extraction-review
description: Use when structured fields extracted from text, OCR, or documents need Jev checks for semantic contradictions and regression-case selection.
license: MIT
---

# Structured extraction review with Jev

Experimental support for development agents. Use semantic evaluation where it adds value; use deterministic tools for mechanical checks.

## Workflow

Read the [shared protocol](references/protocol.md) for evidence preparation, API use and interpretation. The [client](scripts/ask.py) is bundled so this skill can be installed independently.

Provide sanitized source text, the extraction schema and extracted values. This skill evaluates text rather than assuming image input. Distinguish missing evidence, ambiguous labels and contradictions. Validate numbers, date normalization and exact source spans deterministically; use Jev for semantic roles and context. Ask a Choice question per field with supported, contradicted, absent and ambiguous options. Inspect the original span before confirming a finding. Consistency with source text does not prove that the source itself is authentic or correct.

## Synthetic example

Run from this skill directory:

```sh
python3 scripts/ask.py examples/request.json --dry-run
python3 scripts/ask.py examples/request.json
```

The expected category is `contradicted`. Investigate disagreement by examining context, questions and results; do not tune the example merely to force agreement. A synthetic example is a smoke check, not an accuracy benchmark.

Inspired by the [TypeSafe use-case map](https://docs.typesafe.ai/concepts/use-case-map).
