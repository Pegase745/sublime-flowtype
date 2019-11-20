import unittest
from unittest.mock import patch

from FlowType.flowtype.helpers import get_flow_bin


class TestGetFlowBin(unittest.TestCase):
    """Test case for `get_flow_bin` function."""

    @patch("FlowType.flowtype.helpers.get_settings", return_value="path/flow-bin")
    def test_path_exists(self, *_):
        """Return the full path for the Flow binary."""
        flow_path = get_flow_bin()

        self.assertEqual(flow_path, "path/flow-bin")

    @patch("FlowType.flowtype.helpers.get_settings", return_value=None)
    def test_path_not_exists(self, *_):
        """Raise an exception if the path is not set."""
        with self.assertRaises(ValueError):
            get_flow_bin()
