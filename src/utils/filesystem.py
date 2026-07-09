from pathlib import Path


def ensure_directory_exists(path: Path) -> None:
    """
    Creates a directory if it does not exist.
    """
    path.mkdir(
        parents=True,
        exist_ok=True
    )


def file_exists(path: Path) -> bool:
    """
    Checks whether a file exists.
    """
    return path.exists()


def get_file_extension(path: Path) -> str:
    """
    Returns the file extension.
    """
    return path.suffix.lower()


def get_file_size(path: Path) -> int:
    """
    Returns file size in bytes.
    """
    return path.stat().st_size