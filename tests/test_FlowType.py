import unittest
from unittest.mock import patch

from FlowType.FlowType import plugin_loaded


class TestFlowPy(unittest.TestCase):
    """Test case for plugin's main entrypoint."""

    @patch(
        'sublime.version',
        return_value=str(2000)
    )
    def test_bad_sublime_version(self, *_):
        """Raise an error if Sublime Text < 3."""
        with self.assertRaises(RuntimeError):
            plugin_loaded()
