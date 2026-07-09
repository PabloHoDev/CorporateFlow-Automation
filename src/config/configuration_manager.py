from pathlib import Path

import yaml

from src.exceptions.configuration_error import ConfigurationError
from src.models.app_config import AppConfig


class ConfigurationManager:

    def __init__(self, config_path: Path):
        self._config_path = config_path

    def load(self) -> AppConfig:
        """
        Loads and validates application configuration.
        """

        if not self._config_path.exists():
            raise ConfigurationError(
                f"Configuration file not found: {self._config_path}"
            )

        with open(
            self._config_path,
            "r",
            encoding="utf-8"
        ) as file:
            data = yaml.safe_load(file)

        return self._build_config(data)

    def _build_config(
        self,
        data: dict
    ) -> AppConfig:

        try:
            return AppConfig(
                input_directory=Path(
                    data["input_directory"]
                ),
                output_directory=Path(
                    data["output_directory"]
                ),
                backup_directory=Path(
                    data["backup_directory"]
                ),
                log_directory=Path(
                    data["log_directory"]
                ),
                create_backup=data["create_backup"],
                overwrite_existing=data["overwrite_existing"],
                continue_on_error=data["continue_on_error"],
                log_level=data["log_level"],
                save_log_file=data["save_log_file"]
            )

        except KeyError as error:
            raise ConfigurationError(
                f"Missing configuration key: {error}"
            ) from error