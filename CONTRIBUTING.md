# Contributing

Open an issue or pull request with a concrete use case, the proposed change, and how you verified it. Use synthetic or sanitized examples; never include credentials, customer records or proprietary code.

Keep each skill narrowly scoped and independently installable. Changes to prompts should include both useful evidence and an ambiguous or missing-evidence scenario. Report observed model/version and results when running a live evaluation; do not make live API calls part of ordinary CI.

Edit `tools/ask.py` or `tools/protocol.md` for shared changes, run `python3 tools/sync_skills.py`, and commit the generated copies together. Run `python3 -m unittest discover -s tests -v` and `python3 tools/sync_skills.py --check` before submitting.

Do not convert model confidence into automatic permission for destructive actions, releases or external messages. Validate findings with independent evidence.
