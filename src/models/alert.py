from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class AlertSeverity(Enum):
    """
    Define a severidade do alerta.
    """

    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


@dataclass(frozen=True)
class Alert:
    """
    Representa um alerta operacional.
    """

    title: str

    message: str

    severity: AlertSeverity

    source: str

    created_at: datetime = field(
        default_factory=datetime.now
    )

    acknowledged: bool = False

    @property
    def is_critical(self) -> bool:
        """
        Indica se o alerta é crítico.
        """

        return self.severity == AlertSeverity.CRITICAL

    @property
    def requires_action(self) -> bool:
        """
        Define se exige intervenção operacional.
        """

        return self.severity in {
            AlertSeverity.ERROR,
            AlertSeverity.CRITICAL,
        }