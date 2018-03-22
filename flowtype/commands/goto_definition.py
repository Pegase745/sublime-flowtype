import sublime

from .base import BaseCommand
from .exec_flow import ExecFlowCommand
from ..logger import Logger
from ..helpers import prepare_arguments

logger = Logger()


class FlowtypeGotoDefinition(BaseCommand):
    """Run Flow get-def and open file containing definition."""

    def get_cmd(self):
        """Construct cli command."""
        try:
            flow_bin = self.get_flow_bin()
            logger.logger.debug('using flow-bin %s' % flow_bin)
        except ValueError as e:
            logger.logger.error('get_def %s' % e)
            return

        try:
            project_root = self.get_project_root()
        except ValueError as e:
            logger.logger.error('get_def %s' % e)
            return

        arguments = prepare_arguments(self.view)

        cmd = [
            flow_bin, 'get-def',
            '--from', 'nuclide',
            '--root', project_root,
            '--path', arguments.file_name,
            '--quiet', '--json',
            str(arguments.row + 1), str(arguments.col + 1)
        ]

        return cmd

    def handle_process(self, returncode, stdout, error):
        """Handle the output from the threaded process."""
        if type(error) is bytes:
            error = error.decode('utf-8')

        if returncode != 0:
            logger.logger.error('get_def %s' % error)
            return

        logger.logger.debug(stdout)

        if stdout and stdout['path']:
            self.active_window.open_file(
                stdout['path'] +
                ':' + str(stdout['line']) +
                ':' + str(stdout['start']),
                sublime.ENCODED_POSITION |
                False
            )
        else:
            self.view.set_status('flow_type', 'Flow: no definition found')

    def run(self, view):
        """Execute `get_def` command."""
        logger.logger.debug('Running get_def')

        self.view.erase_status('flow_type')
        self.view.erase_regions('flow_type_highlights')

        thread = ExecFlowCommand(
            self.get_cmd(),
            self.get_content()
        )
        thread.start()
        self.check_thread(thread)
