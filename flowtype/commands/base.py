import sublime
import sublime_plugin

from ..helpers import is_js_source, find_in_parent_folders, get_flow_bin


class BaseCommand(sublime_plugin.TextCommand):
    """Common properties and methods for children commands."""

    def get_project_root(self):
        """Return the project root.

        Search for a .flowconfig file and consider its location as the
        project's root.
        """
        file_path = self.active_window.extract_variables()['file_path']
        return find_in_parent_folders('.flowconfig', file_path)

    def get_flow_bin(self):
        """Return the flow binary to use."""
        file_path = self.active_window.extract_variables()['file_path']
        return get_flow_bin(file_path)

    def get_content(self):
        """Return file content."""
        return self.view.substr(sublime.Region(0, self.view.size()))

    def get_cmd(self):
        """Construct cli command."""
        raise NotImplementedError('get_cmd method must be defined')

    def handle_process(self, returncode, stdout, error):
        """Handle the output from the threaded process."""
        raise NotImplementedError('handle_process method must be defined')

    def check_thread(self, thread, i=0, dir=1):
        """Check if the thread is still running."""
        before = i % 8
        after = (7) - before
        if not after:
            dir = -1
        if not before:
            dir = 1
        i += dir

        self.view.set_status(
            'flow_loader',
            'FlowType [%s=%s]' % (' ' * before, ' ' * after)
        )

        if thread.is_alive():
            return sublime.set_timeout(lambda: self.check_thread(
                thread, i, dir), 100)

        self.view.erase_status('flow_loader')
        self.handle_process(thread.returncode, thread.stdout, thread.stderr)

    def is_enabled(self):
        """Enable the command only on Javascript files and has flow pragma."""
        content = self.get_content()
        pragma = '// @flow' in content or '/* @flow */' in content

        return is_js_source(self.view) and pragma

    @property
    def active_window(self):
        """Return active window."""
        return sublime.active_window()
