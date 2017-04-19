"""FlowTypeCompletion."""

import sublime
import sublime_plugin

from .builtintypes import builtintypes


class FlowTypeCompletion(sublime_plugin.EventListener):
    """Abstracts the Flow type autocompletion."""

    @staticmethod
    def get_setting(key, default_value=None):
        """Return the setting for a given key."""
        s = sublime.load_settings('FlowType.sublime-settings')
        return s.get(key, default_value)

    @staticmethod
    def is_source_js(view):
        """Check if a file is a JS source."""
        scope_name = view.scope_name(0).split()
        return 'source.js' in scope_name

    @property
    def show_type_completion(self):
        """Determine whether type autocompletion is enabled."""
        return self.get_setting('show_type_completion', True)

    def on_query_completions(self, view, prefix, locations):
        """Return a list of types when flow typing a variable."""
        if self.show_type_completion:
            if self.is_source_js(view):
                trigger_start = locations[0] - len(prefix)
                line = sublime.Region(
                    view.line(trigger_start).begin(), trigger_start)
                if view.substr(line).strip().endswith(':'):
                    return builtintypes
