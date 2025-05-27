"""
Setup the CLI logger

The logger has a custom formatter which removes sensitive data
"""

import os
import re
import logging
from logging.handlers import RotatingFileHandler

from radiant_fhir_transform_cli.config import SECRETS, LOG_DIR
from radiant_fhir_transform_cli.utils import timestamp

DEFAULT_LOG_FILENAME = "radiant_fhir_transformer"
DEFAULT_LOG_LEVEL = "info"
DEFAULT_LOG_DIR = LOG_DIR

VERBOTEN_PATTERNS = {
    re.escape(os.environ[v]): f"<env['{v}']>"
    for k, v in SECRETS.__dict__.items()
    if not k.startswith("_") and os.environ.get(v)
}

VERBOTEN_PATTERNS['"access_token":".+"'] = '"access_token":"<ACCESS_TOKEN>"'
VERBOTEN_PATTERNS[
    "'Authorization': '.+'"
] = "'Authorization': '<AUTHORIZATION>'"

MB_50 = 52428800
MAX_BYTES = MB_50


class NoTokenFormatter(logging.Formatter):
    """
    A logging formatter which obfuscates sensitive data in the log message
    """

    def format(self, record):
        s = super().format(record)
        for k, v in VERBOTEN_PATTERNS.items():
            s = re.sub(k, v, s)
        return s


DEFAULT_FORMAT = "%(asctime)s - %(name)s" " -  %(levelname)s - %(message)s"
DEFAULT_FORMATTER = NoTokenFormatter(DEFAULT_FORMAT)


def init_logger(log_level=None, log_dir=None, write_logs=True):
    """
    Configure and create the logger

    :param log_level: a string specifying what level of log messages to record
    in the log file. Values are not case sensitive. The list of acceptable
    values are the names of Python's standard lib logging levels.
    (critical, error, warning, info, debug, notset)
    :type log_level: one of logging modules log levels
    """
    log_level = log_level or DEFAULT_LOG_LEVEL
    log_dir = log_dir or DEFAULT_LOG_DIR

    if isinstance(log_level, str):
        log_level = logging._nameToLevel.get(str(log_level).upper())

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(DEFAULT_FORMATTER)

    root = logging.getLogger()
    root.setLevel(log_level)
    root.addHandler(console_handler)

    log_filepath = None
    if write_logs:
        if not log_dir:
            log_dir = DEFAULT_LOG_DIR
        os.makedirs(log_dir, exist_ok=True)

        # Create a new log file named with a timestamp
        filename = f"{DEFAULT_LOG_FILENAME}-{timestamp()}.log"
        log_filepath = os.path.join(log_dir, filename)

        file_handler = RotatingFileHandler(
            log_filepath, mode="w", maxBytes=MB_50
        )
        file_handler.setFormatter(DEFAULT_FORMATTER)

        root.addHandler(file_handler)

    return log_filepath
