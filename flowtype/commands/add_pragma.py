from ..logger import Logger
from .base import BaseCommand

logger = Logger()


class FlowtypeAddPragma(BaseCommand):
    """Add Flow pragma in the beginning of the file."""

    def run(self, edit):
        """Run command."""
        logger.logger.debug('Running add_pragma')

        content = self.get_content()

        if ('// @flow' not in content and '/* @flow */' not in content):
            self.view.insert(edit, 0, "// @flow\n")
        else:
            self.view.erase_status('flow_type')
            self.view.set_status(
                'flow_type', "Flow: pragma already set")
