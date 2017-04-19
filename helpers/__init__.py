"""Set of helpers functions."""

import os
import json
import sublime
import subprocess
from collections import namedtuple

CLIRequirements = namedtuple('CLIRequirements', [
    'filename', 'project_root', 'contents', 'cursor_pos', 'row', 'col'
])


def get_settings():
    """Get plugin settings."""
    return sublime.load_settings('FlowType.sublime-settings')


def debug_print(msg):
    """Print debug message in console."""
    settings = get_settings()
    if settings.get("debug", False):
        print("[DEBUG] FlowType: %s" % msg)


def status_print(msg, view=None):
    """Print message in a flow_type region of status bar."""
    if view is None:
        view = sublime.active_window().active_view()

    view.erase_regions('flow_type')
    view.set_status('flow_type', 'Flow %s' % msg)


def is_js_source(view=None):
    """Check if a file is a JS source."""
    if view is None:
        view = sublime.active_window().active_view()

    scope_name = view.scope_name(0).split()
    return 'source.js' in scope_name


def get_flowbin_options(view=None):
    """Return flowbin input options."""
    if view is None:
        view = sublime.active_window().active_view()

    filename = view.file_name()
    project_root = os.path.dirname(filename)

    cursor_pos = view.sel()[0].begin()
    row, col = view.rowcol(cursor_pos)

    current_contents = view.substr(sublime.Region(0, view.size()))

    return CLIRequirements(
        filename=filename,
        project_root=project_root,
        contents=current_contents,
        cursor_pos=cursor_pos,
        row=row, col=col
    )


def call_flowbin(contents, command):
    """Execute an OS command.

    Subject became clearer thanks to
    https://github.com/tptee/FlowIDE/blob/master/flow-ide.py#L108-L130
    """
    debug_print("call_flowbin %s" % command)

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
    except subprocess.CalledProcessError as e:
        try:
            result = json.loads(e.output.decode('utf-8'))
            os.close(read)
            return result
        except e:
            os.close(read)
            print(e.output)
            return None
