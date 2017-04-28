import sys
import logging
import inspect

from .helpers import singleton, get_settings


class MetaLogger(type):
    """Logger metaclass."""

    def __call__(cls, *args, **kwargs):
        """Set default attributes from the args passed to the object's init."""
        obj = super(MetaLogger, cls).__call__(*args, **kwargs)
        argspec = inspect.getfullargspec(obj.__init__)
        defaults = dict(
            zip(argspec.args[-len(argspec.defaults):], argspec.defaults))
        defaults.update(kwargs)

        for key, val in defaults.items():
            setattr(obj, key, val)

        return obj


@singleton
class Logger(metaclass=MetaLogger):
    """Logger singleton."""

    def __init__(self, logging_configured=False):
        """Set configuration to false on init."""
        pass

    @property
    def logger(self):
        """Return a configured logger."""
        logger = logging.getLogger('flowtype')

        if not self.logging_configured:
            log_level = get_settings('log_level', 'info')
            if log_level not in [
                    'debug', 'info', 'warning', 'error', 'critical']:
                log_level = 'warning'

            logger.propagate = False
            logger.setLevel(logging.__getattribute__(log_level.upper()))

            log_handler = logging.StreamHandler(sys.stdout)
            log_handler.setFormatter(logging.Formatter(
                '%(name)s: %(levelname)s - %(message)s'
            ))
            logger.addHandler(log_handler)

            self.logging_configured = True

        return logger
