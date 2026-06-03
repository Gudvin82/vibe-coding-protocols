import json
from pathlib import Path


def test_schema_exists():
    path = Path('schemas/vcp-card.schema.json')
    assert path.exists()
    payload = json.loads(path.read_text(encoding='utf-8'))
    assert payload['title'] == 'VCP Card'
