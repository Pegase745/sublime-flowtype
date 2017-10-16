from .base import BaseCommand
from .exec_flow import ExecFlowCommand
from ..logger import Logger
from ..helpers import get_flow_bin, prepare_arguments

logger = Logger()


class FlowtypeViewType(BaseCommand):
    """Run Flow type-at-pos and popup type definition."""

    def get_cmd(self):
        """Construct cli command."""
        try:
            flow_bin = get_flow_bin()
        except ValueError as e:
            logger.logger.error('type-at-pos %s' % e)
            return

        try:
            project_root = self.get_project_root()
        except ValueError as e:
            logger.logger.error('type-at-pos %s' % e)
            return

        arguments = prepare_arguments(self.view)

        cmd = [
            flow_bin, 'type-at-pos',
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
            logger.logger.error('type-at-pos %s' % error)
            return

        logger.logger.debug(stdout)

        if stdout:
            self.view.show_popup(stdout['type'].replace(
                '<', '&lt;').replace('>', '&gt;'))
        else:
            self.view.set_status('flow_type', 'Flow: no type found')

    def run(self, view):
        """Execute `type-at-pos` command."""
        logger.logger.debug('Running type-at-pos')

        self.view.erase_status('flow_type')

        thread = ExecFlowCommand(
            self.get_cmd(),
            self.get_content()
        )
        thread.start()
        self.check_thread(thread)
