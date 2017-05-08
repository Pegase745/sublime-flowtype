import sublime_plugin

from ..logger import Logger
from ..helpers import is_js_source

logger = Logger()


class FlowtypeAddPragma(sublime_plugin.TextCommand):
    """Add Flow pragma in the beginning of the file."""

    def is_enabled(self):
        """Enable the command only on Javascript files."""
        return is_js_source(self.view)

    def run(self, edit):
        """Run command."""
        # TODO: check if pragma is not already there
        logger.logger.debug('Running add_pragma')
        self.view.insert(edit, 0, "// @flow\n")
