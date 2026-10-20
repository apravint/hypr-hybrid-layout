import unittest
import os
import tempfile
from unittest.mock import patch
from hypr_hybrid_layout.switcher import apply_mode, toggle_mode, get_current_mode

class TestSwitcher(unittest.TestCase):
    def test_apply_mode_tiling(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            conf = os.path.join(tmpdir, "layout.conf")
            state = os.path.join(tmpdir, "mode")
            with patch("hypr_hybrid_layout.switcher.get_config_path", return_value=conf), \
                 patch("hypr_hybrid_layout.switcher.get_state_path", return_value=state):
                self.assertTrue(apply_mode("tiling"))
                self.assertTrue(os.path.exists(conf))
                with open(conf) as f:
                    content = f.read()
                self.assertIn("rounding = 0", content)
                self.assertEqual(get_current_mode(), "tiling")

    def test_apply_mode_traditional(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            conf = os.path.join(tmpdir, "layout.conf")
            state = os.path.join(tmpdir, "mode")
            with patch("hypr_hybrid_layout.switcher.get_config_path", return_value=conf), \
                 patch("hypr_hybrid_layout.switcher.get_state_path", return_value=state):
                self.assertTrue(apply_mode("traditional"))
                self.assertTrue(os.path.exists(conf))
                with open(conf) as f:
                    content = f.read()
                self.assertIn("rounding = 8", content)
                self.assertIn("windowrulev2 = float", content)
                self.assertEqual(get_current_mode(), "traditional")

    def test_toggle_mode(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            conf = os.path.join(tmpdir, "layout.conf")
            state = os.path.join(tmpdir, "mode")
            with patch("hypr_hybrid_layout.switcher.get_config_path", return_value=conf), \
                 patch("hypr_hybrid_layout.switcher.get_state_path", return_value=state):
                # Start at tiling -> toggle to traditional
                m1 = toggle_mode()
                self.assertEqual(m1, "traditional")
                # Toggle back -> tiling
                m2 = toggle_mode()
                self.assertEqual(m2, "tiling")

if __name__ == "__main__":
    unittest.main()
