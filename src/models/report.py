from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Any

from src.models.processing_result import ProcessingResult


@dataclass
class Report:
    """
    Represents the execution summary of the application.
    """

    started_at: datetime
    finished_at: datetime

    results: list[ProcessingResult] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def duration(self) -> timedelta:
        return self.finished_at - self.started_at

    @property
    def total_files(self) -> int:
        return len(self.results)

    @property
    def successful_files(self) -> int:
        return sum(result.success for result in self.results)

    @property
    def failed_files(self) -> int:
        return sum(not result.success for result in self.results)

    @property
    def processed_records(self) -> int:
        return sum(result.processed_records for result in self.results)

    @property
    def skipped_records(self) -> int:
        return sum(result.skipped_records for result in self.results)

    @property
    def failed_records(self) -> int:
        return sum(result.failed_records for result in self.results)

    @property
    def success_rate(self) -> float:
        if self.total_files == 0:
            return 0.0

        return (self.successful_files / self.total_files) * 100