from FlowType.tests.base import TestCase
from FlowType.flowtype.listeners import FlowTypeListener
from FlowType.flowtype.listeners.builtintypes import builtintypes


class TestOnQueryCompletions(TestCase):
    """Test case for query completions listeners."""

    def test_bad_source(self):
        """Return an empty array if not a JavaScript file."""
        self.view.set_syntax_file("Packages/Python/Python.tmLanguage")
        string = "toto: "
        self.setText(string)

        listener = FlowTypeListener()
        actual = listener.on_query_completions(self.view, 's', [7])

        self.assertEqual(actual, None)

        self.view.set_syntax_file("Packages/JavaScript/JavaScript.tmLanguage")

    def test_complete_builtintype(self):
        """Return a built-in type on completion."""
        string = "toto: "
        self.setText(string)

        listener = FlowTypeListener()
        actual = listener.on_query_completions(self.view, 's', [7])

        self.assertEqual(actual, builtintypes)
