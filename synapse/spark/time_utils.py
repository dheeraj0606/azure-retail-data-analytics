
from datetime import datetime


def current_timestamp():
    """
    Returns current timestamp string.
    Useful for logging and partitioning.
    """
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
