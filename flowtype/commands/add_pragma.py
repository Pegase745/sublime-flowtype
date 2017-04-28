from ..logger import Logger
from .base import BaseCommand

logger = Logger()


class FlowtypeAddPragma(BaseCommand):
    """Add Flow pragma in the beginning of the file."""

    def run(self, edit):
        """Run command."""
        # TODO: check if pragma is not already there
        logger.logger.debug('Running add_pragma')
        self.view.insert(edit, 0, "// @flow\n")
