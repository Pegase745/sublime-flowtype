import unittest
from unittest.mock import MagicMock, Mock

import sublime
from FlowType.flowtype.helpers import prepare_arguments, Arguments


def mock_view(file_path):
    """Mock up a view."""
    view = MagicMock(spec=sublime.View)
    view.file_name = Mock(return_value=file_path)
    view.sel = Mock(return_value=[sublime.Region(4)])
    view.rowcol = Mock(return_value=(0, 0))

    return view


class TestPrepareArguments(unittest.TestCase):
    """Test case for `prepare_arguments` function."""

    def test_complete_args(self):
        """Return a name tuple with arguments."""
        file_path = "/src/myfile"
        expected_arguments = Arguments(
            file_name=file_path, cursor_position=4, row=0, col=0
        )

        view = mock_view(file_path)
        arguments = prepare_arguments(view)

        self.assertTupleEqual(arguments, expected_arguments)
