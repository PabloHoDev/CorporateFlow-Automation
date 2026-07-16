from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class MonitoringSnapshot:
    """
    Representa uma fotografia consolidada
    de uma execução do sistema.
    """

    timestamp: datetime

    execution_time_seconds: float

    files_processed: int

    records_read: int

    records_created: int

    records_updated: int

    records_skipped: int

    errors_count: int

    @property
    def success(self) -> bool:
        """
        Indica se a execução foi concluída sem erros.
        """

        return self.errors_count == 0

    @property
    def processed_records(self) -> int:
        """
        Quantidade total de registros efetivamente tratados.
        """

        return (
            self.records_created +
            self.records_updated +
            self.records_skipped
        )

    @property
    def throughput(self) -> float:
        """
        Registros processados por segundo.
        """

        if self.execution_time_seconds == 0:
            return 0.0

        return (
            self.processed_records /
            self.execution_time_seconds
        )