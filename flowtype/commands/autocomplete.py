from .base import BaseCommand
from .exec_flow import ExecFlowCommand
from ..logger import Logger
from ..helpers import get_flow_bin, prepare_arguments, get_settings
from ..listeners.builtintypes import print_type_format
from ..listeners import FLOW_SUGGESTIONS

logger = Logger()


def build_content_snippet(suggestion):
    """Build snippet for function autocompletion."""
    name = suggestion['name']

    if suggestion['func_details']:
        paramText = ''
        params = suggestion['func_details']['params']

        for param in params:
            if not paramText:
                paramText += param['name']
            else:
                paramText += ', ' + param['name']

        return '{}({})'.format(name, paramText)
    else:
        return name


class FlowtypeAutocomplete(BaseCommand):
    """Run Flow autocomplete and popup type definition."""

    def get_cmd(self):
        """Construct cli command."""
        try:
            flow_bin = get_flow_bin()
        except ValueError as e:
            logger.logger.error('autocomplete %s' % e)
            return

        arguments = prepare_arguments(self.view)

        cmd = [
            flow_bin, 'autocomplete',
            '--from', 'nuclide',
            '--quiet', '--json',
            arguments.file_name,
            str(arguments.row + 1), str(arguments.col + 1)
        ]

        return cmd

    def handle_process(self, returncode, stdout, error):
        """Handle the output from the threaded process."""
        if type(error) is bytes:
            error = error.decode('utf-8')

        if returncode != 0:
            logger.logger.error('autocomplete %s' % error)
            return

        logger.logger.debug(stdout)

        if len(stdout['result']) > 0:
            for suggestion in stdout['result']:
                FLOW_SUGGESTIONS.append(print_type_format(
                    suggestion['name'],
                    build_content_snippet(suggestion),
                    suggestion['type']
                ))

            self.view.run_command('auto_complete', {
                'disable_auto_insert': True,
                'api_completions_only': True,
                'next_completion_if_showing': False,
                'auto_complete_commit_on_tab': True,
            })
        else:
            if (not get_settings('suggest_autocomplete_on_edit', True)):
                self.view.set_status(
                    'flow_type_autocomplete',
                    'Flow: not enough type information to autocomplete')

    def run(self, view):
        """Execute `autocomplete` command."""
        logger.logger.debug('Running autocomplete')

        FLOW_SUGGESTIONS[:] = []

        self.view.erase_status('flow_type_autocomplete')

        thread = ExecFlowCommand(
            self.get_cmd(),
            self.get_content()
        )
        thread.start()
        self.check_thread(thread)
