from FlowType.tests.base import TestCase


class TestAddPragma(TestCase):
    """Test suite for `flowtype_add_pragma` command."""

    def test_no_pragma_if_not_js(self):
        """Do not add a pragma if it's not a JavaScript file."""
        self.view.set_syntax_file("Packages/Python/Python.tmLanguage")
        string = """Lorem ipsum dolor sit amet.
        Ut sit amet gravida nibh."""

        self.setText(string)
        self.view.run_command("flowtype_add_pragma")

        first_row = self.getRow(1)
        self.assertEqual(first_row, "Lorem ipsum dolor sit amet.")

    def test_add_pragma(self):
        """Add a pragma if it's a JavaScript file."""
        string = """Lorem ipsum dolor sit amet.
        Ut sit amet gravida nibh."""

        self.setText(string)
        self.view.run_command("flowtype_add_pragma")

        first_row = self.getRow(1)
        self.assertEqual(first_row, "// @flow")
