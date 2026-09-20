---
name: jev-qa-evidence
description: Use when QA handoffs, release summaries, or completion claims need Jev verification against collected tests and runtime evidence.
license: MIT
---

# QA evidence review with Jev

Experimental support for development agents. Use semantic evaluation where it adds value; use deterministic tools for mechanical checks.

## Workflow

Read the [shared protocol](references/protocol.md) for evidence preparation, API use and interpretation. The [client](scripts/ask.py) is bundled so this skill can be installed independently.

Split a draft into verifiable claims and associate evidence with its environment, timestamp and scope. First check that referenced artifacts exist. Ask a Choice question per claim with supports, contradicts and insufficient options. Distinguish local tests, CI, deployment, runtime execution and persisted state. Inspect discrepancies and narrow unsupported wording. Return each claim, source, model evaluation and independent check. This skill reviews drafts; it does not publish messages or close issues.

## Synthetic example

Run from this skill directory:

```sh
python3 scripts/ask.py examples/request.json --dry-run
python3 scripts/ask.py examples/request.json
```

The expected category is `insufficient`. Investigate disagreement by examining context, questions and results; do not tune the example merely to force agreement. A synthetic example is a smoke check, not an accuracy benchmark.

Inspired by the [TypeSafe use-case map](https://docs.typesafe.ai/concepts/use-case-map).
