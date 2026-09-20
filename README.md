# Jev Dev Skills

Five experimental agent skills that use [TypeSafe Jev](https://docs.typesafe.ai/concepts/use-case-map) to support software development and testing. Skills, examples and documentation are in English.

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
npx skills add Pleo2/jev-dev-skills --skill jev-test-coverage
```

Replace the name with another skill from the table, or omit `--skill` to select skills interactively. Each folder is self-contained, including its Python client and shared protocol. You may also copy a folder into your agent's supported skills directory.

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
