"""
All configuration values for the CLI
"""

import os


# File paths and directories
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname((__file__))))
ROOT_DATA_DIR = os.path.join(ROOT_DIR, "data")
LOG_DIR = os.path.join(ROOT_DATA_DIR, "logs")


class SECRETS:
    """
    Used in logger initialization to obfuscate sensitive env variables
    """


def get_config() -> dict:
    """
    Return configuration parameters
    """
    return {}
