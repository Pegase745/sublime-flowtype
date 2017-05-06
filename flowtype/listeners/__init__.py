import sublime
import sublime_plugin

from .builtintypes import builtintypes
from ..helpers import get_settings
from ..logger import Logger

logger = Logger()


class FlowTypeListener(sublime_plugin.EventListener):
    """Abstracts the plugin listeners."""

    def on_query_completions(self, view, prefix, locations):
        """Suggest a list of types for a variable."""
        if get_settings('show_type_completion', True):
            loc = locations[0]
            if not view.match_selector(loc, 'source.js'):
                return []

            logger.logger.debug('Running autocompletion')

            trigger_start = loc - len(prefix)
            line = sublime.Region(
                view.line(trigger_start).begin(), trigger_start)
            if view.substr(line).strip().endswith(':'):
                # TODO: only built-int starting with prefix
                return builtintypes
