from .base import BaseCommand
from .exec_flow import ExecFlowCommand
from ..logger import Logger
from ..helpers import get_flow_bin, prepare_arguments

logger = Logger()


class FlowtypeCoverage(BaseCommand):
    """Run Flow coverage and highlight uncovered lines."""

    def get_cmd(self):
        """Construct cli command."""
        try:
            flow_bin = get_flow_bin()
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
            total = covered + uncovered
            percentage = (covered * 100.0) / total

            self.view.set_status(
                'flow_type',
                'Flow: {}% coverage with {}/{} uncovered lines'
                .format(round(percentage, 2), uncovered, covered))
        else:
            self.view.set_status('flow_type', 'Flow: no type found')

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
