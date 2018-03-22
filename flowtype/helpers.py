import re
import os
import json
import time
import subprocess
from collections import namedtuple

import sublime

Arguments = namedtuple('Arguments', [
    'file_name', 'cursor_position', 'row', 'col'
])

FLOWTYPE = {
    'LAST_ERROR_CHECK': time.time(),
}


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
    try:
        file_extension = os.path.splitext(view.file_name())[1:][0]
    except AttributeError as e:
        file_extension = ''

    return 'source.js' in scope_name or file_extension in ('.js', '.flow')


def get_settings(setting, default=None):
    """Get settings."""
    settings = sublime.load_settings('FlowType.sublime-settings')

    return settings.get(setting, default)


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
            file_path = current_dir
            break
        else:
            if current_dir == parent_dir:
                raise ValueError(
                    "No %s was found in any parent folder" % file_name)
            else:
                current_dir = parent_dir

    return file_path


def find_executable(name, file_path):
    """
    Return the path of an executable
        :param name: name of the executable we're searching for
    """
    result = None
    paths = list(filter(None, list(reversed(os.defpath.split(os.pathsep)))))
    node_module_path = find_in_parent_folders("package.json", file_path)

    paths.insert(0, "%s/node_modules/.bin" % (node_module_path))

    for outerpath in paths:
        for innerpath, _, _ in os.walk(outerpath):
            path = os.path.join(innerpath, name)
            if os.access(path, os.X_OK):
                result = os.path.normpath(path)
                break
        else:
            continue
        break

    return result


def get_flow_bin(file_path):
    """Return the full path for the Flow binary."""
    flow_bin = get_settings('flow_bin_path', None)

    if not flow_bin:
        flow_bin = find_executable("flow", file_path)
        if not flow_bin:
            raise ValueError('Path value is missing for flow_bin_path setting')

    return flow_bin


_hdr_pat = re.compile("^@@ -(\d+),?(\d+)? \+(\d+),?(\d+)? @@$")


def apply_patch(s, patch, revert=False):
    """Apply unified diff patch to string s to recover newer string.

    If revert is True, treat s as the newer string, recover older string.
    Readapted from http://stackoverflow.com/a/40967337/2588498
    """
    s = s.splitlines(True)
    p = patch.splitlines(True)
    t = ''
    i = sl = 1 # start at line 2 # noqa
    (midx, sign) = (1, '+') if not revert else (3, '-')
    while i < len(p) and p[i].startswith(("---", "+++")):
        i += 1  # skip header lines
    while i < len(p):
        m = _hdr_pat.match(p[i])
        if not m:
            raise Exception("Cannot process diff")
        i += 1
        l = int(m.group(midx)) - 1 + (m.group(midx + 1) == '0')  # noqa
        t += ''.join(s[sl:l])
        sl = l
        while i < len(p) and p[i][0] != '@':
            if i + 1 < len(p) and p[i + 1][0] == '\\':
                line = p[i][:-1]
                i += 2
            else:
                line = p[i]
                i += 1
            if len(line) > 0:
                if line[0] == sign or line[0] == ' ':
                    t += line[1:]
                sl += (line[0] != sign)
    t += ''.join(s[sl:])
    return t
