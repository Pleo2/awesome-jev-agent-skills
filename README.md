# JevScope — AI Agent Skills for Code Review & Testing

**Sharper reviews. Stronger evidence.**

[![Checks](https://github.com/Pleo2/jevscope/actions/workflows/checks.yml/badge.svg)](https://github.com/Pleo2/jevscope/actions/workflows/checks.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](tools/ask.py)

JevScope is an open-source collection of **AI agent skills for code review, software testing, debugging, structured extraction, and QA evidence verification**. Powered by [TypeSafe Jev](https://docs.typesafe.ai/concepts/use-case-map), it gives coding agents focused semantic checks with structured answers and probabilities.

Use it to inspect a pull request against an invariant, identify missing test scenarios, triage an error, or check whether a release claim is supported by evidence. Your coding agent verifies the findings with code and tests.

[Install](#install) · [Skills](#available-ai-agent-skills) · [Examples](#development-workflow-examples) · [Contribute](CONTRIBUTING.md) · [Español](README.es.md)

## Available AI agent skills

| Skill | Purpose |
| --- | --- |
| [jev-diagnose-failures](skills/jev-diagnose-failures/SKILL.md) | Triage failures and choose the next diagnostic check |
| [jev-test-coverage](skills/jev-test-coverage/SKILL.md) | Find missing behavioral test scenarios |
| [jev-review-diff](skills/jev-review-diff/SKILL.md) | Review changes against explicit invariants |
| [jev-extraction-review](skills/jev-extraction-review/SKILL.md) | Review structured extraction against source text |
| [jev-qa-evidence](skills/jev-qa-evidence/SKILL.md) | Check completion claims against evidence |

## Install

Install a skill with the Skills CLI, choosing your agent when prompted:

```sh
npx skills add Pleo2/jevscope --skill jev-test-coverage
```

Replace the name with another skill from the table, or omit `--skill` to select skills interactively. Each folder is self-contained, including its Python client and shared protocol. You may also copy a folder into your agent's supported skills directory.

## Development workflow examples

Give your coding agent a concrete request and the relevant skill:

- **AI code review:** “Use `jev-review-diff` to check whether this change preserves user access controls. Verify any finding against the callers.”
- **Test gap analysis:** “Use `jev-test-coverage` to compare these acceptance criteria with the test assertions and identify missing scenarios.”
- **Debugging:** “Use `jev-diagnose-failures` to prioritize which layer to inspect from these sanitized error logs.”
- **Extraction validation:** “Use `jev-extraction-review` to compare these extracted fields with their source document.”
- **QA verification:** “Use `jev-qa-evidence` to check whether this release summary is supported by the attached test and runtime evidence.”

These workflows support general software projects without depending on a particular application, framework or business domain.

## Use

Requires Python 3.9+ and a TypeSafe API key for live requests. The client uses only Python's standard library. Configure `TYPESAFE_API_KEY` in your environment, or pass an explicit private env file. Never commit a real key.

From an installed skill directory:

```sh
python3 scripts/ask.py examples/request.json --dry-run
python3 scripts/ask.py examples/request.json
# Alternative to an environment variable:
python3 scripts/ask.py examples/request.json --env-file /private/path/typesafe.env
```

Ask your agent to use the relevant skill for a concrete task. It prepares a minimal sanitized request and verifies useful Jev findings with code, sources or executed tests. Responses include the resolved model, probabilities, token usage and elapsed time.

Jev evaluations are advisory. They do not establish test coverage, source authenticity, deployment success or permission to mutate external systems. No universal confidence thresholds are imposed. API calls may incur TypeSafe charges; dry-runs and repository tests make no API requests.

The examples are small synthetic cases designed for smoke checks. This is a smoke check, not a benchmark of real-world accuracy. Model outputs can change; investigate discrepancies instead of treating examples as infallible assertions.

## Frequently asked questions

### What is JevScope?

A set of five installable development skills, each with instructions, a synthetic example and a small Python client for TypeSafe Jev. It is an independent community project.

### Can I use it with Codex or Claude Code?

Use the Skills CLI and select your agent, or copy a skill folder into the skills directory supported by your agent. JevScope uses `SKILL.md` instructions and a Python client; it does not require an editor extension or an MCP server. Follow your agent's skill discovery rules.

### Does it replace tests, static analysis or human review?

No. It adds semantic evaluations to an existing development workflow. Keep linters, type checking, test execution and independent review as the evidence for correctness.

### Is JevScope free and open source?

The repository is MIT licensed. Live evaluations require a TypeSafe API key and may incur service charges. Local validation and CI run without paid API calls.

## Maintain

The canonical client and protocol live in `tools/`. After editing either:

```sh
python3 tools/sync_skills.py
python3 -m unittest discover -s tests -v
python3 tools/sync_skills.py --check
```

CI checks offline behavior and that every packaged skill has current shared files. It never requires a secret or calls Jev. See [CONTRIBUTING.md](CONTRIBUTING.md) for contributions.

## License and attribution

MIT for this repository's skills and client. This is an independent community project, not an official TypeSafe product. It builds on the public [API documentation](https://docs.typesafe.ai/api.md), [use-case map](https://docs.typesafe.ai/concepts/use-case-map), and [citation verification cookbook](https://docs.typesafe.ai/cookbooks/citation_check.md). The upstream TypeSafe skill is not bundled. Hosted Jev models and services are subject to their own terms; the MIT license does not cover them.
