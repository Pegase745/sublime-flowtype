"""This plugin for Sublime Text is an attempt in making a great Flow IDE."""

import sys


if sys.version_info < (3, 0):
    from commands import *  # noqa
    from listener import *  # noqa
else:
    from .commands import *  # noqa
    from .listener import *  # noqa
