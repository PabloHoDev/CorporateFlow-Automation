from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AppConfig:
    """
    Represents the application's runtime configuration.

    This object is created by ConfigurationManager and shared
    across the entire application lifecycle.
    """

    # Directories
    input_directory: Path
    output_directory: Path
    backup_directory: Path
    log_directory: Path

    # Processing settings
    create_backup: bool
    overwrite_existing: bool
    continue_on_error: bool

    # Logging settings
    log_level: str
    save_log_file: bool