from pathlib import Path

from src.models.app_config import AppConfig


def test_should_create_app_config():

    config = AppConfig(
        input_directory=Path("./input"),
        output_directory=Path("./output"),
        backup_directory=Path("./backups"),
        log_directory=Path("./logs"),
        create_backup=True,
        overwrite_existing=False,
        continue_on_error=True,
        log_level="INFO",
        save_log_file=True
    )

    assert config.create_backup is True
    assert config.log_level == "INFO"
    assert config.input_directory == Path("./input")