import unittest

import sublime


class TestCase(unittest.TestCase):
    """Base test suite used to manipulate a file."""

    def setUp(self):
        """Create a file to work with on each test."""
        self.view = sublime.active_window().new_file()
        # make sure we have a window to work with
        s = sublime.load_settings("Preferences.sublime-settings")
        s.set("close_windows_when_empty", False)
        self.view.set_syntax_file("Packages/JavaScript/JavaScript.tmLanguage")

    def tearDown(self):
        """Close the file after running the test suite."""
        if self.view:
            # a scratch buffer never reports as being dirty
            self.view.set_scratch(True)
            try:
                self.view.erase_status("flow_type")
                self.view.erase_regions("flow_type_highlights")
            except Exception as e:
                return
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

    def setText(self, string):
        """Insert a given string text into file."""
        self.view.run_command("insert", {"characters": string})

    def getRow(self, row):
        """Return content of a given row number."""
        return self.view.substr(self.view.line(self.view.text_point(row - 1, 0)))
