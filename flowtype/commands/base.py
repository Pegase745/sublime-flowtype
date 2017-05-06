import sublime_plugin
from ..helpers import is_js_source


class BaseCommand(sublime_plugin.TextCommand):
    """Common properties and methods for children commands."""

    def is_enabled(self):
        """Enable the command only on Javascript files."""
        return is_js_source(self.view)
