from os.path import isfile
import subprocess
import sys
import unittest


class TestDrakeVisualizerBazel(unittest.TestCase):
    # Drake Visualizer is disabled for at least as long as it takes to
    # transition Drake and VTK 8.2 to Python 3.9 or some alternative solution
    # is found, see https://github.com/RobotLocomotion/drake/issues/14650 for
    # updates.
    @unittest.skipIf(
        sys.platform == "darwin",
        "Drake Visualizer is disabled on macOS, see https://git.io/Jt1BG "
        "for updates")
    def test_help(self):
        """Ensure we can call drake_visualizer --help in Bazel."""
        bin_path = "tools/drake_visualizer"
        self.assertTrue(isfile(bin_path), bin_path)
        text = subprocess.check_output([bin_path, "--help"], encoding="utf8")

        # N.B. This should be kept in sync with
        # `drake_visualizer_installed_help_test`.
        print(text)
        # Test for nominal help string.
        self.assertIn("usage: drake-visualizer ", text)
        self.assertNotIn(
            "drake-visualizer: error: unrecognized arguments", text)
        # Test for modifications in help text.
        self.assertIn("--use_builtin_scripts", text)
        self.assertIn("Options: all,", text)
