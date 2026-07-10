from datetime import datetime


def current_timestamp() -> datetime:
    """
    Returns current datetime.
    """
    return datetime.now()


def format_duration(seconds: float) -> str:
    """
    Formats execution duration.
    """

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    return (
        f"{int(hours):02d}:"
        f"{int(minutes):02d}:"
        f"{int(seconds):02d}"
    )