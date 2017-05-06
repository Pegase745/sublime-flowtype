import json
import unittest
import subprocess
from unittest.mock import patch

from FlowType.flowtype.helpers import run_flow


class TestRunFlow(unittest.TestCase):
    """Test case for `run_flow` function."""

    @patch(
        'subprocess.check_output',
        return_value=bytes(json.dumps({"dumb": False}), encoding='utf-8')
    )
    def test_valid_command(self, *_):
        """Return result after running a valid command."""
        result = run_flow(['dumb', 'command'], 'fake contents')

        self.assertEqual(result, {"dumb": False})

    @patch(
        'subprocess.check_output',
        side_effect=subprocess.CalledProcessError(0, '')
    )
    def test_command_fails(self, *_):
        """Return an error after command returns an exit stat."""
        with self.assertRaises(subprocess.CalledProcessError):
            run_flow(['bad', 'command'], 'fake contents')
