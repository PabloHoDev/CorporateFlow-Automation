from src.models.health_status import HealthStatus


def test_health_status_default_values():
    """
    Deve criar um HealthStatus saudável por padrão.
    """

    health = HealthStatus()

    assert health.is_healthy is True
    assert health.errors == []
    assert health.warnings == []
    assert health.has_errors is False
    assert health.has_warnings is False
    assert health.checked_at is not None


def test_add_error_changes_health_status():
    """
    Deve marcar o ambiente como não saudável ao adicionar erro.
    """

    health = HealthStatus()

    health.add_error(
        "Diretório input não encontrado."
    )

    assert health.is_healthy is False
    assert health.has_errors is True
    assert len(health.errors) == 1

    assert (
        "Diretório input não encontrado."
        in health.errors
    )


def test_add_warning_keeps_health_status():
    """
    Warnings não devem tornar o ambiente inválido.
    """

    health = HealthStatus()

    health.add_warning(
        "Diretório backups está vazio."
    )

    assert health.is_healthy is True
    assert health.has_warnings is True
    assert len(health.warnings) == 1

    assert (
        "Diretório backups está vazio."
        in health.warnings
    )


def test_multiple_errors():
    """
    Deve armazenar múltiplos erros.
    """

    health = HealthStatus()

    health.add_error("Erro 1")
    health.add_error("Erro 2")
    health.add_error("Erro 3")

    assert len(health.errors) == 3
    assert health.has_errors is True
    assert health.is_healthy is False


def test_multiple_warnings():
    """
    Deve armazenar múltiplos avisos.
    """

    health = HealthStatus()

    health.add_warning("Warning 1")
    health.add_warning("Warning 2")

    assert len(health.warnings) == 2
    assert health.has_warnings is True