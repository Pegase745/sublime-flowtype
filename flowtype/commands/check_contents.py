import sublime

from .base import BaseCommand
from ..logger import Logger
from ..spinner import Spinner
from ..helpers import get_flow_bin, prepare_arguments, run_flow

logger = Logger()
spinner = Spinner()


class FlowtypeCheckContents(BaseCommand):
    """Run Flow check-contents."""

    def run(self, edit):
        """Run command with async timeout."""
        sublime.set_timeout_async(self.run_async)

    def run_async(self):
        """Run command."""
        spinner.start()

        description_by_row = {}

        logger.logger.debug('Running check_contents')

        try:
            flow_bin = get_flow_bin()
        except ValueError as e:
            spinner.stop()
            logger.logger.error('check_contents %s' % e)
            return

        arguments = prepare_arguments(self.view)

        self.view.erase_regions('flow_type_highlights')

        try:
            result = run_flow([
                flow_bin, 'check-contents',
                '--from', 'nuclide',
                '--json', arguments.file_name
            ], arguments.contents)
        except Exception as e:
            spinner.stop()
            logger.logger.error('check_contents %s' % e)
            return

        logger.logger.debug(result)

        if result:
            passed = result.get('passed', False)
            errors = result.get('errors', [])
            flow_version = result.get('flowVersion', '')

            # No errors
            if passed:
                spinner.stop()
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

            spinner.stop()

            self.view.erase_status('flow_type')
            self.view.set_status(
                'flow_type', 'Flow %s: %s error(s) -> %s' %
                (flow_version, len(errors), description_by_row))
