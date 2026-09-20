---
name: jev-test-coverage
description: Use when acceptance criteria and proposed or existing tests need a Jev review for missing behavioral scenarios.
license: MIT
---

# Behavioral test coverage with Jev

Experimental support for development agents. Use semantic evaluation where it adds value; use deterministic tools for mechanical checks.

## Workflow

Read the [shared protocol](references/protocol.md) for evidence preparation, API use and interpretation. The [client](scripts/ask.py) is bundled so this skill can be installed independently.

Map each acceptance criterion to actual test assertions. Separate proposed tests from executed tests. Consider relevant success, failure, boundary, feature-flag, authorization and retry cases. Ask one Choice question per criterion with covered, partial, missing and insufficient options. Inspect the assertions before confirming a gap, then add justified regression tests and run focused checks. Model probabilities are not code coverage percentages.

## Synthetic example

Run from this skill directory:

```sh
python3 scripts/ask.py examples/request.json --dry-run
python3 scripts/ask.py examples/request.json
```

The expected category is `missing`. Investigate disagreement by examining context, questions and results; do not tune the example merely to force agreement. A synthetic example is a smoke check, not an accuracy benchmark.

Inspired by the [TypeSafe use-case map](https://docs.typesafe.ai/concepts/use-case-map).
