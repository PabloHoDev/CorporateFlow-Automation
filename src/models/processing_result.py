from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Any

from src.models.input_file import InputFile


@dataclass
class ProcessingResult:
    """
    Represents the result of processing an input file.
    """

    # Source file
    input_file: InputFile

    # Execution result
    success: bool

    # Timing information
    started_at: datetime
    finished_at: datetime

    # Processing metrics
    processed_records: int = 0
    skipped_records: int = 0
    failed_records: int = 0

    # Error handling
    error_message: str | None = None
    exception_type: str | None = None

    # Additional information
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def duration(self) -> timedelta:
        """
        Returns the total execution time.
        """
        return self.finished_at - self.started_at