from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from src.models.app_config import AppConfig
from src.models.processing_result import ProcessingResult


@dataclass
class ExecutionContext:
    """
    Represents the runtime state of a single execution.
    """

    configuration: AppConfig

    started_at: datetime

    results: list[ProcessingResult] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)