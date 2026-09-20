import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('client', ROOT / 'tools/ask.py')
client = importlib.util.module_from_spec(spec)
spec.loader.exec_module(client)


class ClientTests(unittest.TestCase):
    def test_env_file_is_parsed_without_execution(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {}, clear=True):
            path = Path(tmp) / 'key.env'
            path.write_text("export TYPESAFE_API_KEY='synthetic-key'\n")
            self.assertEqual(client.read_key(path), 'synthetic-key')
            path.write_text('TYPESAFE_API_KEY=$(echo never-executed)\n')
            self.assertEqual(client.read_key(path), '$(echo never-executed)')

    def test_environment_takes_precedence(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {'TYPESAFE_API_KEY': 'environment-key'}, clear=True):
            path = Path(tmp) / 'key.env'
            path.write_text('TYPESAFE_API_KEY=file-key\n')
            self.assertEqual(client.read_key(path), 'environment-key')

    def test_missing_key(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ValueError):
                client.read_key(None)

    def test_redirects_are_blocked(self):
        self.assertIsNone(client.NoRedirect().redirect_request(None, None, 302, '', {}, 'https://example.com'))

    def test_all_packaged_examples_validate_without_network(self):
        for skill in (ROOT / 'skills').iterdir():
            with self.subTest(skill=skill.name):
                result = subprocess.run([sys.executable, str(skill / 'scripts/ask.py'), str(skill / 'examples/request.json'), '--dry-run'], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(result.stdout)['status'], 'valid')

    def invoke(self, payload, key='fake-test-key'):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'request.json'
            path.write_text(json.dumps(payload))
            out, err = io.StringIO(), io.StringIO()
            with patch.object(sys, 'argv', ['ask.py', str(path)]), patch.dict(os.environ, {'TYPESAFE_API_KEY': key}, clear=True), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                status = client.main()
            return status, out.getvalue(), err.getvalue()

    def test_empty_questions_rejected_before_network(self):
        with patch.object(client.urllib.request, 'build_opener') as opener:
            status, _, _ = self.invoke({'state': 'test', 'questions': {}})
            self.assertEqual(status, 1)
            opener.assert_not_called()

    def test_key_in_payload_rejected_before_network(self):
        with patch.object(client.urllib.request, 'build_opener') as opener:
            status, out, err = self.invoke({'state': 'fake-test-key', 'questions': {'q': {'type': 'noul', 'instructions': 'Is this a test?'}}})
            self.assertEqual(status, 1)
            self.assertNotIn('fake-test-key', out + err)
            opener.assert_not_called()

    def test_http_error_body_is_not_printed(self):
        with patch.object(client.urllib.request, 'build_opener') as opener:
            opener.return_value.open.side_effect = urllib.error.HTTPError('https://api.typesafe.ai/v1/systemone', 401, 'private server detail', {}, None)
            status, out, err = self.invoke({'state': 'test', 'questions': {'q': {'type': 'noul', 'instructions': 'Is this a test?'}}})
            self.assertEqual(status, 1)
            self.assertEqual(json.loads(err)['http_status'], 401)
            self.assertNotIn('private server detail', out + err)


if __name__ == '__main__':
    unittest.main()
