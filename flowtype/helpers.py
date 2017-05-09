import os
import json
import subprocess
from collections import namedtuple

import sublime

Arguments = namedtuple('Arguments', [
    'file_name', 'cursor_position', 'row', 'col'
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
    file_extension = os.path.splitext(view.file_name())[1:][0]

    return 'source.js' in scope_name or file_extension in ('.js', '.flow')


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
    cursor_position = view.sel()[0].begin()
    row, col = view.rowcol(cursor_position)

    return Arguments(
        file_name=file_name,
        cursor_position=cursor_position,
        row=row,
        col=col
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

        decoded_output = output.decode('utf-8')

        clean_output = decoded_output[decoded_output.find('{\"'):]

        result = json.loads(clean_output)

        os.close(read)
        return result
    except subprocess.CalledProcessError as err:
        raise err


def find_in_parent_folders(file_name, current_dir):
    """Search for a given filename.

    Starting from a given path and in parent paths until file is found.
    """
    file_path = ""

    while True:
        file_list = os.listdir(current_dir)
        parent_dir = os.path.dirname(current_dir)
        if file_name in file_list:
            file_path = "%s/%s" % (current_dir, file_name)
            break
        else:
            if current_dir == parent_dir:
                raise ValueError(
                    "No %s was found in any parent folder" % file_name)
                break
            else:
                current_dir = parent_dir

    return file_path
