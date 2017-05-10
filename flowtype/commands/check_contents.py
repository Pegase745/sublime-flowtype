import sublime

from .base import BaseCommand
from .exec_flow import ExecFlowCommand
from ..logger import Logger
from ..helpers import get_flow_bin, prepare_arguments, get_settings

logger = Logger()


class FlowtypeCheckContents(BaseCommand):
    """Run Flow check-contents."""

    def get_cmd(self):
        """Construct cli command."""
        try:
            flow_bin = get_flow_bin()
        except ValueError as e:
            logger.logger.error('check_contents %s' % e)
            return

        arguments = prepare_arguments(self.view)

        cmd = [
            flow_bin, 'check-contents',
            '--from', 'nuclide',
            '--quiet', '--json', arguments.file_name
        ]

        return cmd

    def handle_process(self, returncode, stdout, error):
        """Handle the output from the threaded process."""
        if type(error) is bytes:
            error = error.decode('utf-8')

        if returncode != 0:
            logger.logger.error('check_contents %s' % error)
            return

        passed = stdout.get('passed', False)
        errors = stdout.get('errors', [])
        flow_version = stdout.get('flowVersion', '')

        # No errors
        if passed:
            self.view.erase_status('flow_type')
            self.view.set_status(
                'flow_type', 'Flow %s: no errors' % flow_version)
            return

        # Errors
        regions = []
        self.points = []
        panel_errors = []
        for error in errors:
            legend = []
            full_description = []
            messages = error.get('message', [])
            operation = messages[0]

            if operation:
                row = int(operation['line']) - 1
                col = int(operation['start']) - 1
                endcol = int(operation['end'])

                start = self.view.text_point(row, col)
                stop = self.view.text_point(row, endcol)

                # Keep track to link from quick panel
                self.points.append(stop)

                regions.append(sublime.Region(start, stop))

            for message in messages:
                legend.append(message['descr'])

            full_description.append('{} {}'.format(
                row + 1, operation['context']))
            full_description.append(' '.join(legend))

            panel_errors.append(full_description)

        self.view.add_regions(
            'flow_type_highlights',
            regions, 'string', 'dot',
            sublime.DRAW_NO_FILL
        )

        self.view.erase_status('flow_type')
        self.view.set_status(
            'flow_type', 'Flow {}: {} error{}'.format(
                flow_version, len(errors), 's' if len(errors) > 1 else ''))

        self.viewport_pos = self.view.viewport_position()
        self.selection = list(self.view.sel())

        if (not get_settings('check_contents_on_edit', True)):
            self.active_window.show_quick_panel(
                panel_errors,
                on_select=self.select_error,
                on_highlight=self.select_error
            )

    def select_error(self, index):
        """On select handler for the quick panel."""
        if index != -1:
            point = self.points[index]
            self.select_lint_region(sublime.Region(point, point))
        else:
            self.view.set_viewport_position(self.viewport_pos)
            self.view.sel().clear()
            self.view.sel().add_all(self.selection)

    def select_lint_region(self, region):
        """Select and scroll to the first marked given region."""
        sel = self.view.sel()
        sel.clear()
        sel.add(region)

        self.view.show_at_center(region)

    def run(self, view):
        """Execute `check_contents` command."""
        logger.logger.debug('Running check_contents')

        self.view.erase_regions('flow_type_highlights')

        thread = ExecFlowCommand(
            self.get_cmd(),
            self.get_content()
        )
        thread.start()
        self.check_thread(thread)
