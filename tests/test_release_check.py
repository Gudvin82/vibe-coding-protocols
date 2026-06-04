from __future__ import annotations

import unittest

from vcp_cli.release_check import payload


class ReleaseCheckTests(unittest.TestCase):
    def test_release_check_payload_status(self) -> None:
        data = payload()
        self.assertIn(data["status"], {"pass", "warn", "block"})
        self.assertIn("distribution_doc", data["checked"])


if __name__ == "__main__":
    unittest.main()
