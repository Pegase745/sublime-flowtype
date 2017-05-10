import sublime
import sublime_plugin

from .builtintypes import builtintypes
from ..helpers import get_settings
from ..logger import Logger

logger = Logger()

FLOW_SUGGESTIONS = []


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
            if view.substr(line).strip().endswith(
                    (':', '.', '(', '{', '[', ',')):
                if (get_settings('complete_with_builtintypes', True)):
                    # TODO: only built-in starting with prefix
                    return FLOW_SUGGESTIONS + builtintypes
                return FLOW_SUGGESTIONS

    def on_selection_modified_async(self, view):
        """Erase highlighted regions and status when modifying selection."""
        view.erase_regions('flow_type_highlights')
        view.erase_status('flow_type')

        if (get_settings('suggest_autocomplete_on_edit', True)):
            # TODO: only run autocomplete if word ends with : and .
            view.run_command('flowtype_autocomplete')

        if (get_settings('check_contents_on_edit', False)):
            view.run_command('flowtype_check_contents')

    def on_post_save_async(self, view):
        """Erase highlighted regions and status when saving file."""
        view.erase_regions('flow_type_highlights')
        view.erase_status('flow_type')

        if (get_settings('check_contents_on_save', True)):
            view.run_command('flowtype_check_contents')
