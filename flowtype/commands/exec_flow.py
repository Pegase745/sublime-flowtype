import os
import json
import threading
import subprocess

import sublime


class ExecFlowCommand(threading.Thread):
    """Threaded class used for running flow commands in a different thread.

    The subprocess must be threaded so we don't lockup the UI.
    """

    def __init__(self, cmd, content):
        """Initialize with the command and the file content to send."""
        self.cmd = cmd
        self.content = content
        self.stdout = None
        self.returncode = 0
        self.stderr = None

        threading.Thread.__init__(self)

    def run(self):
        """Execute the command in a subprocess."""
        read, write = os.pipe()
        os.write(write, str.encode(self.content))
        os.close(write)

        try:
            output = subprocess.check_output(
                self.cmd,
                shell=sublime.platform() == 'windows',
                stdin=read,
                stderr=subprocess.STDOUT
            )

            if type(output) is bytes:
                output = output.decode('utf-8')

            try:
                self.stdout = json.loads(output)
            except ValueError as e:
                self.stdout = output

            os.close(read)
        except subprocess.CalledProcessError as err:
            self.stderr = str(err)
            self.returncode = 1
