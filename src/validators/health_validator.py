import sys
from pathlib import Path

from src.models.health_status import HealthStatus


class HealthValidator:

    REQUIRED_DIRECTORIES = [
        "input",
        "output",
        "logs",
        "backups",
        "config"
    ]

    MINIMUM_PYTHON_VERSION = (3, 12)

    def validate(self) -> HealthStatus:
        """
        Executa todas as verificações do ambiente.
        """

        status = HealthStatus()

        self._validate_python_version(status)

        self._validate_directories(status)

        self._validate_write_permissions(status)

        return status

    def _validate_python_version(
        self,
        status: HealthStatus
    ) -> None:

        if sys.version_info < self.MINIMUM_PYTHON_VERSION:

            status.add_error(
                (
                    f"Python "
                    f"{self.MINIMUM_PYTHON_VERSION[0]}."
                    f"{self.MINIMUM_PYTHON_VERSION[1]}"
                    f" ou superior é obrigatório."
                )
            )

    def _validate_directories(
        self,
        status: HealthStatus
    ) -> None:

        for directory in self.REQUIRED_DIRECTORIES:

            if not Path(directory).exists():

                status.add_error(
                    f"Diretório obrigatório não encontrado: {directory}"
                )

    def _validate_write_permissions(
        self,
        status: HealthStatus
    ) -> None:

        writable_directories = [
            "output",
            "logs",
            "backups"
        ]

        for directory in writable_directories:

            path = Path(directory)

            if path.exists() and not path.is_dir():

                status.add_error(
                    f"{directory} existe mas não é um diretório."
                )

                continue

            if path.exists() and not path.stat().st_mode:

                status.add_warning(
                    f"Não foi possível validar permissões em {directory}"
                )