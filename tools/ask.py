#!/usr/bin/env python3
"""Send one bounded TypeSafe evaluation; never print credentials or server error bodies."""
import argparse
import json
import os
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.request

DEFAULT_ENV = None


def read_key(path):
    values = dict(os.environ)
    if path is not None and path.exists():
        for line in path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line.startswith('export '):
                line = line[7:].strip()
            if '=' not in line:
                continue
            name, value = line.split('=', 1)
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            else:
                value = re.split(r'\s+#', value, maxsplit=1)[0].strip()
            values.setdefault(name.strip(), value)
    for name in ('TYPESAFE_API_KEY', 'TYPESAFE_AI_API_KEY', 'JEV_API_KEY'):
        if values.get(name):
            return values[name]
    raise ValueError('No supported API key configured')


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('request', type=Path)
    parser.add_argument('--env-file', type=Path, default=DEFAULT_ENV)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        payload = json.loads(args.request.read_text())
        if not isinstance(payload, dict) or 'state' not in payload:
            raise ValueError('Request needs state and questions')
        questions = payload.get('questions')
        if not isinstance(questions, dict) or not 1 <= len(questions) <= 20:
            raise ValueError('Use 1 to 20 questions per request')
        for q in questions.values():
            if not isinstance(q, dict) or q.get('type') not in ('choice', 'noul', 'score') or not q.get('instructions'):
                raise ValueError('Invalid question')
            if q['type'] == 'choice' and (not isinstance(q.get('criteria'), dict) or not 2 <= len(q['criteria']) <= 255):
                raise ValueError('Choice needs 2 to 255 options')
            if q['type'] == 'score' and (not isinstance(q.get('criteria'), list) or not 2 <= len(q['criteria']) <= 10):
                raise ValueError('Score needs 2 to 10 levels')
        payload.setdefault('model', 'jev-latest')
        data = json.dumps(payload).encode()
        if len(data) > 65536:
            raise ValueError('Reduce request to at most 64 KiB')
        if args.dry_run:
            print(json.dumps({'status': 'valid', 'questions': len(questions), 'bytes': len(data)}))
            return 0
        key = read_key(args.env_file)
        if key in data.decode():
            raise ValueError('Credential found in request')
        req = urllib.request.Request('https://api.typesafe.ai/v1/systemone', data=data,
            headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'}, method='POST')
        start = time.monotonic()
        with urllib.request.build_opener(NoRedirect).open(req, timeout=30) as response:
            result = json.load(response)
            answers = result.get('answers', {})
            if set(answers) != set(questions) or any(answers[k].get('type') != questions[k]['type'] for k in questions):
                raise ValueError('Response question mismatch')
            output = {'http_status': response.status, 'elapsed_seconds': round(time.monotonic()-start, 3),
                      'model': result.get('model'), 'answers': answers, 'usage': result.get('usage')}
            print(json.dumps(output, ensure_ascii=False).replace(key, '[REDACTED]'))
        return 0
    except urllib.error.HTTPError as exc:
        print(json.dumps({'status': 'http_error', 'http_status': exc.code}), file=sys.stderr)
    except Exception as exc:
        print(json.dumps({'status': 'failed', 'error_type': type(exc).__name__}), file=sys.stderr)
    return 1


if __name__ == '__main__':
    sys.exit(main())
