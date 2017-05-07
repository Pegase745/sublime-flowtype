import time
import sublime
import threading

from .helpers import singleton


@singleton
class Spinner(object):
    """Spinner singleton."""

    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        """Define the spinner cursors."""
        while 1:
            for cursor in '|/-\\':
                yield cursor

    def __init__(self, delay=None):
        """Initialize a spinner."""
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay):
            self.delay = delay

    def spinner_task(self):
        """Show spinning cursor in the status bar."""
        active_view = sublime.active_window().active_view()

        while self.busy:
            active_view.erase_status('flow_type')
            active_view.set_status(
                'flow_type',
                'Flow is running [%s]' % next(self.spinner_generator))
            time.sleep(self.delay)

    def start(self):
        """Start spinning in a thread."""
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def stop(self):
        """Stop spinning."""
        self.busy = False
        time.sleep(self.delay)
