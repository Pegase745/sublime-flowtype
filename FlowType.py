import sublime

from .flowtype.commands import *  # noqa
from .flowtype.listeners import *  # noqa


def plugin_loaded():
    """Raise an error if Sublime Text < 3."""
    if int(sublime.version()) < 3000:
        raise RuntimeError('FlowType plugin works with Sublime Text 3 only.')
