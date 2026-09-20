"""Bundle shared files into independently installable skills."""
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
stale = []
for skill in sorted((root / 'skills').iterdir()):
    if not (skill / 'SKILL.md').is_file():
        continue
    for source, target in [('ask.py', 'scripts/ask.py'), ('protocol.md', 'references/protocol.md')]:
        data = (root / 'tools' / source).read_bytes()
        path = skill / target
        if args.check:
            if not path.exists() or path.read_bytes() != data:
                stale.append(str(path.relative_to(root)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
if stale:
    raise SystemExit('Outdated bundled files: ' + ', '.join(stale))
print('Shared skill files are synchronized.')
