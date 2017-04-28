from FlowType.tests.base import TestCase
from FlowType.flowtype.helpers import is_js_source


class TestIsJsSource(TestCase):
    """Test case for `is_js_source` function."""

    def test_js_source(self):
        """Return true if it's a JavaScript source."""
        actual = is_js_source(self.view)

        self.assertTrue(actual)

    def test_non_js_source(self):
        """Return false if it's not a JS source."""
        self.view.set_syntax_file("Packages/Python/Python.tmLanguage")

        actual = is_js_source(self.view)

        self.assertFalse(actual)
