---
name: jev-diagnose-failures
description: Use when logs, failing tests, or service errors need semantic triage with Jev before choosing the next diagnostic check.
license: MIT
---

# Failure triage with Jev

Experimental support for development agents. Use semantic evaluation where it adds value; use deterministic tools for mechanical checks.

## Workflow

Read the [shared protocol](references/protocol.md) for evidence preparation, API use and interpretation. The [client](scripts/ask.py) is bundled so this skill can be installed independently.

Collect the exact error, environment, execution stage, recent changes and a working control when available. Ask a Choice question to prioritize the failing layer; use independent Noul questions for potentially coexisting causes. Distinguish observations from hypotheses and unknowns. Verify the suggested cause with actual traces or a focused reproduction before reporting a root cause. Return the evidence, hypothesis, and next useful check.

## Synthetic example

Run from this skill directory:

```sh
python3 scripts/ask.py examples/request.json --dry-run
python3 scripts/ask.py examples/request.json
```

The expected category is `upstream`. Investigate disagreement by examining context, questions and results; do not tune the example merely to force agreement. A synthetic example is a smoke check, not an accuracy benchmark.

Inspired by the [TypeSafe use-case map](https://docs.typesafe.ai/concepts/use-case-map).
