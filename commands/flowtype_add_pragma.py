"""flowtype_add_pragma command."""

import sublime_plugin

from ..helpers import is_js_source


class FlowtypeAddPragma(sublime_plugin.TextCommand):
    """Add Flow pragma in the beginning of the file."""

    def is_enabled(self):
        """Enable command for a Javascript source."""
        return is_js_source(self.view)

    def run(self, edit):
        """Run command."""
        # TODO: check if pragma is not already there
        self.view.insert(edit, 0, "// @flow\n")
