from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class ExecutionMetrics:
    """
    Representa as métricas coletadas durante uma execução.
    """

    start_time: datetime = field(
        default_factory=datetime.now
    )

    end_time: Optional[datetime] = None

    files_processed: int = 0

    records_read: int = 0

    records_created: int = 0

    records_updated: int = 0

    records_skipped: int = 0

    errors_count: int = 0


    def finish(self) -> None:
        """
        Finaliza a execução registrando
        o horário de término.
        """

        self.end_time = datetime.now()


    @property
    def execution_time_seconds(self) -> float:
        """
        Retorna o tempo total de execução em segundos.
        """

        if not self.end_time:
            return 0.0


        return (
            self.end_time - self.start_time
        ).total_seconds()