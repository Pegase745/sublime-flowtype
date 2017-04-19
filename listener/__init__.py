"""FlowTypeListener."""

import sublime
import subprocess
import sublime_plugin

from .builtintypes import builtintypes
from ..helpers import debug_print, status_print, is_js_source, get_settings


class FlowTypeListener(sublime_plugin.EventListener):
    """Abstracts the plugin listeners."""

    @property
    def settings(self):
        """Use plugin settings as class property."""
        return get_settings()

    @staticmethod
    def debug_print(msg):
        """Print message in console."""
        return debug_print("listener: %s" % msg)

    def on_load(self, view):
        """Print Flow bin version after file is loaded."""
        self.debug_print('get flow binary version')
        flow_bin = self.settings.get("flow_bin_path")

        try:
            output = subprocess.check_output([flow_bin, 'version'])
            result = output.decode('utf-8')
            start = result.find('version ') + 8
            end = result.find('\n', start)
            status_print("version is %s" % result[start:end])
        except Exception as e:
            self.debug_print(e)
            raise e

    def on_query_completions(self, view, prefix, locations):
        """Suggest a list of types for a variable."""
        self.debug_print('autocomplete')
        if self.settings.get("show_type_completion", True):
            if is_js_source(view):
                trigger_start = locations[0] - len(prefix)
                line = sublime.Region(
                    view.line(trigger_start).begin(), trigger_start)
                if view.substr(line).strip().endswith(':'):
                    return builtintypes
