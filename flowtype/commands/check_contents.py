import sublime

from .base import BaseCommand
from .exec_flow import ExecFlowCommand
from ..logger import Logger
from ..helpers import get_flow_bin, prepare_arguments

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
            '--json', arguments.file_name
        ]

        return cmd

    def handle_process(self, returncode, stdout, error):
        """Handle the output from the threaded process."""
        if type(error) is bytes:
            error = error.decode('utf-8')

        if returncode != 0:
            logger.logger.error('check_contents %s' % error)
            return

        description_by_row = {}

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
        for error in errors:
            rows = []
            description = ''

            operation = error.get('message')[0]
            comment = error.get('message')[1]
            if operation:
                row = int(operation['line']) - 1
                col = int(operation['start']) - 1
                endcol = int(operation['end'])

                start = self.view.text_point(row, col)
                stop = self.view.text_point(row, endcol)

                regions.append(sublime.Region(start, stop))
                rows.append(row)
            description = '{} {}'.format(
                operation['descr'], comment['descr'])
            for row in rows:
                row_description = description_by_row.get(row)
                if not row_description:
                    description_by_row[row + 1] = description

        logger.logger.debug(description_by_row)

        self.view.add_regions(
            'flow_type_highlights',
            regions, 'string', 'dot',
            sublime.DRAW_SOLID_UNDERLINE
        )

        self.view.erase_status('flow_type')
        self.view.set_status(
            'flow_type', 'Flow %s: %s error(s) -> %s' %
            (flow_version, len(errors), description_by_row))

    def run(self, edit):
        """Execute `check_contents` command."""
        logger.logger.debug('Running check_contents')

        self.view.erase_regions('flow_type_highlights')

        thread = ExecFlowCommand(
            self.get_cmd(),
            self.get_content()
        )
        thread.start()
        self.check_thread(thread)
