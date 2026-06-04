from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from vcp_cli import plugins_cmd


class PluginCommandTests(unittest.TestCase):
    def test_list_payload_finds_example_plugins(self) -> None:
        data = plugins_cmd.list_payload()
        self.assertTrue(data["ok"])
        self.assertGreaterEqual(len(data["items"]), 1)

    def test_validate_payload_accepts_valid_metadata(self) -> None:
        path = Path("examples/plugins/example-readiness-check.plugin.json")
        data = plugins_cmd.validate_payload(str(path))
        self.assertTrue(data["ok"])
        self.assertFalse(data["execution_occurs"])

    def test_validate_payload_rejects_missing_fields(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.plugin.json"
            path.write_text(json.dumps({"id": "bad"}), encoding="utf-8")
            data = plugins_cmd.validate_payload(str(path))
            self.assertFalse(data["ok"])
            self.assertTrue(data["errors"])


if __name__ == "__main__":
    unittest.main()
