from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class InputFile:
    """
    Represents an input file discovered by the application.
    """

    # File identification
    file_name: str
    stem: str
    extension: str
    path: Path

    # Physical information
    size_bytes: int
    created_at: datetime
    modified_at: datetime

    # Processing information
    discovered_at: datetime
    status: str = "DISCOVERED"
    metadata: dict[str, Any] = field(default_factory=dict)