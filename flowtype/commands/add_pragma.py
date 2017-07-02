from ..logger import Logger
from .base import BaseCommand
from ..helpers import is_js_source

logger = Logger()


class FlowtypeAddPragma(BaseCommand):
    """Add Flow pragma in the beginning of the file."""

    def is_enabled(self):
        """Enable the command only on Javascript files and has flow pragma."""
        content = self.get_content()
        no_pragma = '// @flow' not in content and '/* @flow */' not in content

        return is_js_source(self.view) and no_pragma

    def run(self, edit):
        """Run command."""
        logger.logger.debug('Running add_pragma')

        self.view.insert(edit, 0, "// @flow\n\n")
