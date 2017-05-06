import os
import json
import subprocess
from collections import namedtuple

import sublime

Arguments = namedtuple('Arguments', [
    'file_name', 'cursor_position', 'row', 'col', 'contents'
])


def singleton(cls):
    """A decorator to make a class into a singleton."""
    _instances = {}

    def getinstance():
        if cls not in _instances:
            _instances[cls] = cls()
        return _instances[cls]
    return getinstance


def is_js_source(view):
    """Check if it's a Javascript file."""
    scope_name = view.scope_name(0).split()
    return 'source.js' in scope_name


def get_settings(setting, default=None):
    """Get settings."""
    settings = sublime.load_settings('FlowType.sublime-settings')

    return settings.get(setting, default)


def get_flow_bin():
    """Return the full path for the Flow binary."""
    flow_bin = get_settings('flow_bin_path', None)

    if not flow_bin:
        raise ValueError('Path value is missing for flow_bin_path setting')

    return flow_bin


def prepare_arguments(view):
    """Prepare arguments to be sent to the Flow binary."""
    file_name = view.file_name()
    # TODO: rename into selection instead
    cursor_position = view.sel()[0].begin()
    row, col = view.rowcol(cursor_position)
    contents = view.substr(sublime.Region(0, view.size()))

    return Arguments(
        file_name=file_name,
        cursor_position=cursor_position,
        row=row,
        col=col,
        contents=contents
    )


def run_flow(command, contents):
    """Run Flow command on a given contents."""
    read, write = os.pipe()
    os.write(write, str.encode(contents))
    os.close(write)

    try:
        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT, stdin=read
        )

        result = json.loads(output.decode('utf-8'))

        os.close(read)
        return result
    except subprocess.CalledProcessError as err:
        raise err
