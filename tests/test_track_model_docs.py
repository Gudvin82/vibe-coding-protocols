from __future__ import annotations

import unittest
from pathlib import Path


class TrackModelDocsTests(unittest.TestCase):
    def test_track_model_docs_keep_two_core_tracks(self) -> None:
        for rel in ["docs/track-model.md", "docs/two-track-model.md", "AGENTS.md", "AI_EVALUATION_GUIDE.md"]:
            text = Path(rel).read_text(encoding="utf-8")
            self.assertIn("New Project Track", text)
            self.assertIn("Existing Project Track", text)
            self.assertIn("MVP-to-Launch", text)

    def test_ai_docs_do_not_call_mvp_to_launch_third_core_track(self) -> None:
        for rel in ["AGENTS.md", "AI_EVALUATION_GUIDE.md", "llms.txt", "llms-full.txt", "ai.txt"]:
            text = Path(rel).read_text(encoding="utf-8").lower()
            self.assertNotIn("mvp-to-launch is a third core track", text)
            self.assertNotIn("mvp-to-launch is a separate core track", text)


if __name__ == "__main__":
    unittest.main()
