"""flowtype_run_type_checker command."""

import sublime_plugin

from ..helpers import (
    debug_print,
    is_js_source,
    call_flowbin,
    get_settings,
    get_flowbin_options,
    status_print
)


class FlowtypeRunTypeChecker(sublime_plugin.TextCommand):
    """Run typechecker on file contents."""

    @property
    def settings(self):
        """Use plugin settings as class property."""
        return get_settings()

    @staticmethod
    def debug_print(msg):
        """Print message in console."""
        return debug_print("check_contents: %s" % msg)

    def is_enabled(self):
        """Enable command for a Javascript source."""
        return is_js_source(self.view)

    def run(self, edit):
        """Run command."""
        self.debug_print('typecheck file')
        flow_bin = self.settings.get("flow_bin_path")

        options = get_flowbin_options(self.view)

        result = call_flowbin(options.contents, [
            flow_bin, 'check-contents',
            '--from', 'nuclide',
            '--json',
            options.filename
        ])

        self.debug_print(result)

        if result:
            if result['passed']:
                status_print("found no errors")
                return
