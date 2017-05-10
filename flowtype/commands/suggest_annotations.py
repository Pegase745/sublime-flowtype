from .base import BaseCommand
from .exec_flow import ExecFlowCommand
from ..logger import Logger
from ..helpers import get_flow_bin, prepare_arguments, apply_patch

logger = Logger()


class FlowtypeSuggestAnnotations(BaseCommand):
    """Run Flow suggest and return type annotations."""

    def get_cmd(self):
        """Construct cli command."""
        try:
            flow_bin = get_flow_bin()
        except ValueError as e:
            logger.logger.error('suggest %s' % e)
            return

        arguments = prepare_arguments(self.view)

        cmd = [
            flow_bin, 'suggest',
            '--from', 'nuclide',
            '--quiet', arguments.file_name
        ]

        return cmd

    def handle_process(self, returncode, stdout, error):
        """Handle the output from the threaded process."""
        if type(error) is bytes:
            error = error.decode('utf-8')

        if returncode != 0:
            logger.logger.error('suggest %s' % error)
            return

        logger.logger.debug(stdout)

        if stdout:
            new_contents = apply_patch(self.get_content(), stdout)
            f = open(self.view.file_name(), 'w')
            f.write(new_contents)
            f.close()

            # add pragma because applying patch removes it
            self.view.run_command('flowtype_add_pragma')
        else:
            self.view.set_status('flow_type', 'Flow: no suggestion found')

    def run(self, view):
        """Execute `suggest` command."""
        logger.logger.debug('Running suggest')

        self.view.erase_status('flow_type')
        self.view.erase_regions('flow_type_highlights')

        thread = ExecFlowCommand(
            self.get_cmd(),
            self.get_content()
        )
        thread.start()
        self.check_thread(thread)
