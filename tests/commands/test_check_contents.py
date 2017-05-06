import json
from unittest.mock import patch

import sublime

from FlowType.tests.base import TestCase


class TestCheckContents(TestCase):
    """Test suite for `flowtype_check_contents` command."""

    @patch(
        'subprocess.check_output',
        return_value=bytes(json.dumps(
            {"errors": [], "passed": True, "flowVersion": "0.45.0"}),
            encoding='utf-8')
    )
    @patch(
        'sublime.View.file_name',
        return_value='/path/to/lorem.js'
    )
    def test_no_errors(self, *_):
        """Return no errors in the status bar."""
        string = """Lorem ipsum dolor sit amet.
        Ut sit amet gravida nibh."""

        self.setText(string)
        self.view.run_command("flowtype_check_contents")

        actual = self.view.get_status('flow_type')
        expected = "Flow 0.45.0: no errors"

        self.assertEqual(actual, expected)

    @patch(
        'subprocess.check_output',
        return_value=bytes(json.dumps(
            {
                'flowVersion': '0.45.0',
                'passed': False,
                'errors': [
                    {
                        'kind': 'infer',
                        'message': [
                            {
                                'descr': 'identifier `gravida`',
                                'path': '/path/to/lorem.js',
                                'context': '  status: gravida,',
                                'start': 13,
                                'endline': 2,
                                'end': 19,
                                'loc': {
                                    'source': '/path/to/lorem.js',
                                    'end': {
                                        'column': 19,
                                        'line': 2,
                                        'offset': 48
                                    },
                                    'type': 'SourceFile',
                                    'start': {
                                        'column': 13,
                                        'line': 2,
                                        'offset': 40
                                    }
                                },
                                'type': 'Blame',
                                'line': 2
                            }, {
                                'descr': 'Could not resolve name',
                                'path': '',
                                'context': None,
                                'start': 1,
                                'endline': 0,
                                'end': 0,
                                'type': 'Comment',
                                'line': 0
                            }
                        ],
                        'level': 'error'
                    }
                ]
            }), encoding='utf-8')
    )
    @patch(
        'sublime.View.file_name',
        return_value='/path/to/lorem.js'
    )
    def test_highlight_region_on_errors(self, *_):
        """Highlight the region in error."""
        string = """Lorem ipsum dolor sit amet.
        Ut sit amet gravida nibh."""

        self.setText(string)
        self.view.run_command("flowtype_check_contents")

        actual = self.view.get_status('flow_type')
        expected = "Flow 0.45.0: 1 error(s) -> {2: 'identifier `gravida`" + \
            " Could not resolve name'}"

        self.assertEqual(actual, expected)

        error_regions = self.view.get_regions('flow_type_highlights')

        self.assertEqual(error_regions[0], sublime.Region(40, 47))

    @patch(
        'FlowType.flowtype.helpers.get_settings',
        return_value=None
    )
    def test_bad_flow_path(self, *_):
        """Return if flow path is bad or not set."""
        string = """Lorem ipsum dolor sit amet.
        Ut sit amet gravida nibh."""

        self.setText(string)
        self.view.run_command("flowtype_check_contents")

        actual = self.view.get_status('flow_type')
        expected = ""  # nothing happens, only logger.error

        self.assertEqual(actual, expected)

    @patch(
        'subprocess.check_output',
        side_effect=Exception(
            "Can't convert 'NoneType' object to str implicitly")
    )
    def test_bad_arguments(self, *_):
        """Return if bad arguments are sent to binary."""
        string = """Lorem ipsum dolor sit amet.
        Ut sit amet gravida nibh."""

        self.setText(string)
        self.view.run_command("flowtype_check_contents")

        actual = self.view.get_status('flow_type')
        expected = ""  # nothing happens, only logger.error

        self.assertEqual(actual, expected)
