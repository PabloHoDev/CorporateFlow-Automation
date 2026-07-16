from pathlib import Path

from src.models.health_status import HealthStatus
from src.validators.health_validator import HealthValidator


def test_validate_returns_health_status():
    """
    Deve retornar um objeto HealthStatus.
    """

    validator = HealthValidator()

    result = validator.validate()

    assert isinstance(
        result,
        HealthStatus
    )


def test_missing_directory_creates_error(
    monkeypatch
):
    """
    Deve registrar erro caso um diretório
    obrigatório não exista.
    """

    validator = HealthValidator()

    monkeypatch.setattr(
        validator,
        "REQUIRED_DIRECTORIES",
        ["fake_directory"]
    )

    result = validator.validate()

    assert result.is_healthy is False

    assert result.has_errors is True

    assert len(result.errors) > 0


def test_existing_directories_are_valid(
    tmp_path,
    monkeypatch
):
    """
    Deve considerar ambiente saudável
    quando todos os diretórios existem.
    """

    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    logs_dir = tmp_path / "logs"
    backups_dir = tmp_path / "backups"
    config_dir = tmp_path / "config"

    input_dir.mkdir()
    output_dir.mkdir()
    logs_dir.mkdir()
    backups_dir.mkdir()
    config_dir.mkdir()

    validator = HealthValidator()

    monkeypatch.setattr(
        validator,
        "REQUIRED_DIRECTORIES",
        [
            input_dir,
            output_dir,
            logs_dir,
            backups_dir,
            config_dir
        ]
    )

    result = validator.validate()

    assert result.has_errors is False


def test_invalid_python_version(
    monkeypatch
):
    """
    Deve gerar erro caso a versão do Python
    seja inferior à mínima exigida.
    """

    validator = HealthValidator()

    monkeypatch.setattr(
        validator,
        "MINIMUM_PYTHON_VERSION",
        (99, 0)
    )

    result = validator.validate()

    assert result.has_errors is True