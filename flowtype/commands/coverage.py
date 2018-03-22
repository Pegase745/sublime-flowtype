import sublime

from .base import BaseCommand
from .exec_flow import ExecFlowCommand
from ..logger import Logger
from ..helpers import prepare_arguments

logger = Logger()


class FlowtypeCoverage(BaseCommand):
    """Run Flow coverage and highlight uncovered lines."""

    def get_cmd(self):
        """Construct cli command."""
        try:
            flow_bin = self.get_flow_bin()
            logger.logger.debug('using flow-bin %s' % flow_bin)
        except ValueError as e:
            logger.logger.error('coverage %s' % e)
            return

        arguments = prepare_arguments(self.view)

        cmd = [
            flow_bin, 'coverage',
            '--from', 'nuclide',
            '--quiet', '--json', arguments.file_name
        ]

        return cmd

    def handle_process(self, returncode, stdout, error):
        """Handle the output from the threaded process."""
        self.view.erase_regions('flow_type_uncovered')

        if type(error) is bytes:
            error = error.decode('utf-8')

        if returncode != 0:
            logger.logger.error('coverage %s' % error)
            return

        logger.logger.debug(stdout)

        if stdout:
            expressions = stdout['expressions']
            covered = expressions['covered_count']
            uncovered = expressions['uncovered_count']
            uncovered_locs = expressions['uncovered_locs']
            total = covered + uncovered
            percentage = (covered * 100.0) / total

            self.view.set_status(
                'flow_type',
                'Flow: {}% coverage with {}/{} uncovered lines'
                .format(round(percentage, 2), uncovered, covered))

            if len(uncovered_locs) > 0:
                # Uncovered regions
                regions = []
                for location in uncovered_locs:
                    row_start = int(location['start']['line']) - 1
                    col_start = int(location['start']['column']) - 1
                    row_end = int(location['end']['line']) - 1
                    col_end = int(location['end']['column'])

                    start = self.view.text_point(row_start, col_start)
                    stop = self.view.text_point(row_end, col_end)

                    regions.append(sublime.Region(start, stop))

                self.view.add_regions(
                    'flow_type_uncovered',
                    regions, 'comment', 'bookmark',
                    sublime.DRAW_SQUIGGLY_UNDERLINE
                )

        else:
            self.view.set_status('flow_type', 'Flow: coverage is not possible')

    def run(self, view):
        """Execute `coverage` command."""
        logger.logger.debug('Running coverage')

        self.view.erase_status('flow_type')

        thread = ExecFlowCommand(
            self.get_cmd(),
            self.get_content()
        )
        thread.start()
        self.check_thread(thread)
