"""Print hello world."""

import sublime_plugin


class Example(sublime_plugin.TextCommand):
    """Print hello world."""

    def run(self, edit):
        """Run command."""
        self.view.insert(edit, 0, "Hello, World!")
