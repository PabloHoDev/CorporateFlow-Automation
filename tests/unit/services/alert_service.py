from typing import List

from src.models.alert import Alert, AlertSeverity


class AlertService:
    """
    Responsável pelo gerenciamento dos alertas do sistema.
    """

    def __init__(self) -> None:
        self._alerts: List[Alert] = []

    def register(self, alert: Alert) -> None:
        """
        Registra um novo alerta.
        """

        self._alerts.append(alert)

    def get_all(self) -> List[Alert]:
        """
        Retorna todos os alertas registrados.
        """

        return self._alerts.copy()

    def get_by_severity(
        self,
        severity: AlertSeverity
    ) -> List[Alert]:
        """
        Retorna alertas de uma severidade específica.
        """

        return [
            alert
            for alert in self._alerts
            if alert.severity == severity
        ]

    def get_critical_alerts(self) -> List[Alert]:
        """
        Retorna todos os alertas críticos.
        """

        return self.get_by_severity(
            AlertSeverity.CRITICAL
        )

    def count(self) -> int:
        """
        Retorna a quantidade total de alertas.
        """

        return len(self._alerts)

    def count_by_severity(
        self,
        severity: AlertSeverity
    ) -> int:
        """
        Retorna a quantidade de alertas
        para determinada severidade.
        """

        return len(
            self.get_by_severity(
                severity
            )
        )

    def has_critical_alerts(self) -> bool:
        """
        Indica se existem alertas críticos ativos.
        """

        return (
            self.count_by_severity(
                AlertSeverity.CRITICAL
            ) > 0
        )

    def clear(self) -> None:
        """
        Remove todos os alertas registrados.
        """

        self._alerts.clear()