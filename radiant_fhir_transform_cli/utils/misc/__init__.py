"""
Miscellaneous Utility Functions
"""

import datetime
import importlib
import os
import re
import time
from urllib.parse import urlparse

LOCAL_HOSTS = {
    "localhost",
    "127.0.0.1",
}


def timestamp() -> str:
    """
    Helper to create an ISO 8601 formatted string that represents local time
    and includes the timezone info.
    """
    # Calculate the offset taking into account daylight saving time
    # https://stackoverflow.com/questions/2150739/iso-time-iso-8601-in-python
    if time.localtime().tm_isdst:
        utc_offset_sec = time.altzone
    else:
        utc_offset_sec = time.timezone
    utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
    t = (
        datetime.datetime.now()
        .replace(tzinfo=datetime.timezone(offset=utc_offset))
        .isoformat()
    )

    return str(t)


def is_localhost(url: str) -> bool:
    """
    Determine whether url is on localhost
    """
    url = url.strip("/")
    host = urlparse(url).netloc.split(":")[0]
    return (host in LOCAL_HOSTS) or (
        any([url.startswith(h) for h in LOCAL_HOSTS])
    )


def delete_safety_check(url: str, error_msg: str = None) -> None:
    """
    Check if the url is on localhost and raise an exception if it is.

    This method is used in delete operations where you want to protect against
    deletions on hosts other than localhost
    """
    if is_localhost(url):
        # If localhost, we are allowed delete
        pass
    else:
        if not error_msg:
            error_msg = (
                f"❌ Cannot delete from {url} because env variable"
                " DELETE_SAFETY_CHECK=True. Resources that are not in"
                f" {LOCAL_HOSTS} will not be deleted. To disable safety check,"
                " set DELETE_SAFETY_CHECK=False in your environment"
            )
        raise ValueError(error_msg)


def elapsed_time_hms(start_time: float) -> str:
    """
    Gets the time elapsed since `start_time` in hh:mm:ss string format.

    Args:
        start_time (datetime.datetime): The starting time from which to calculate the elapsed time.

    Returns:
        str: A time string formatted as hh:mm:ss.
    """
    elapsed = time.time() - start_time
    return time.strftime("%H:%M:%S", time.gmtime(elapsed))


def import_module_from_file(filepath: str):
    """
    Import a Python module given a filepath
    """
    module_name = os.path.basename(filepath).split(".")[0]
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    imported_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(imported_module)

    return imported_module


def ensure_directory_exists(file_path: str):
    directory = os.path.dirname(file_path)
    if not os.path.isdir(directory):
        os.makedirs(directory)


def camel_to_snake(name: str) -> str:
    """
    Converts a CamelCase or camelCase string to snake_case.

    Args:
        name: The CamelCase string.

    Returns:
        str: The converted snake_case string.
    """
    # Add underscore before uppercase letters (excluding first char)
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)

    # Handle multiple uppercase sequences (e.g. JSONParser -> json_parser)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
