from datetime import datetime
from typing import List

from src.models.execution_metrics import ExecutionMetrics
from src.models.monitoring_snapshot import MonitoringSnapshot


class MonitoringService:
    """
    Responsável pela consolidação e acompanhamento
    das métricas operacionais do sistema.
    """

    def __init__(self) -> None:
        self._snapshots: List[MonitoringSnapshot] = []

    def register_execution(
        self,
        metrics: ExecutionMetrics
    ) -> MonitoringSnapshot:
        """
        Registra uma execução finalizada.
        """

        snapshot = MonitoringSnapshot(
            timestamp=datetime.now(),
            execution_time_seconds=metrics.execution_time_seconds,
            files_processed=metrics.files_processed,
            records_read=metrics.records_read,
            records_created=metrics.records_created,
            records_updated=metrics.records_updated,
            records_skipped=metrics.records_skipped,
            errors_count=metrics.errors_count,
        )

        self._snapshots.append(snapshot)

        return snapshot

    def get_total_executions(self) -> int:
        """
        Retorna a quantidade total de execuções registradas.
        """

        return len(self._snapshots)

    def get_success_rate(self) -> float:
        """
        Calcula a taxa de sucesso das execuções.
        """

        if not self._snapshots:
            return 0.0

        successful = sum(
            1
            for snapshot in self._snapshots
            if snapshot.errors_count == 0
        )

        return successful / len(self._snapshots)

    def get_average_execution_time(self) -> float:
        """
        Retorna o tempo médio de execução.
        """

        if not self._snapshots:
            return 0.0

        total_time = sum(
            snapshot.execution_time_seconds
            for snapshot in self._snapshots
        )

        return total_time / len(self._snapshots)

    @property
    def snapshots(self) -> List[MonitoringSnapshot]:
        """
        Retorna os snapshots registrados.
        """

        return self._snapshots.copy()