from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class HealthStatus:
    """
    Representa o resultado do Health Check do sistema.
    """

    is_healthy: bool = True

    errors: List[str] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)

    checked_at: datetime = field(
        default_factory=datetime.now
    )

    def add_error(self, message: str) -> None:
        """
        Adiciona um erro ao resultado da validação.
        """

        self.errors.append(message)

        self.is_healthy = False

    def add_warning(self, message: str) -> None:
        """
        Adiciona um aviso ao resultado da validação.
        """

        self.warnings.append(message)

    @property
    def has_errors(self) -> bool:
        """
        Indica se existem erros registrados.
        """

        return len(self.errors) > 0

    @property
    def has_warnings(self) -> bool:
        """
        Indica se existem avisos registrados.
        """

        return len(self.warnings) > 0