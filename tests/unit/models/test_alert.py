from datetime import datetime

from src.models.alert import (
    Alert,
    AlertSeverity,
)


def test_alert_creation():
    """
    Deve criar um alerta corretamente.
    """

    alert = Alert(
        title="Erro de teste",
        message="Mensagem de teste",
        severity=AlertSeverity.ERROR,
        source="TestService",
    )

    assert alert.title == "Erro de teste"
    assert alert.message == "Mensagem de teste"
    assert alert.severity == AlertSeverity.ERROR
    assert alert.source == "TestService"
    assert alert.acknowledged is False
    assert isinstance(
        alert.created_at,
        datetime
    )


def test_critical_alert():
    """
    Deve identificar alertas críticos.
    """

    alert = Alert(
        title="Erro crítico",
        message="Falha grave",
        severity=AlertSeverity.CRITICAL,
        source="HealthValidator",
    )

    assert alert.is_critical is True
    assert alert.requires_action is True


def test_error_alert_requires_action():
    """
    Alertas de erro devem exigir ação.
    """

    alert = Alert(
        title="Erro",
        message="Arquivo não encontrado",
        severity=AlertSeverity.ERROR,
        source="ExcelService",
    )

    assert alert.is_critical is False
    assert alert.requires_action is True


def test_warning_alert():
    """
    Warnings não devem ser críticos.
    """

    alert = Alert(
        title="Lentidão",
        message="Execução acima do esperado",
        severity=AlertSeverity.WARNING,
        source="MonitoringService",
    )

    assert alert.is_critical is False
    assert alert.requires_action is False


def test_info_alert():
    """
    Alertas informativos não exigem ação.
    """

    alert = Alert(
        title="Execução concluída",
        message="Processamento finalizado.",
        severity=AlertSeverity.INFO,
        source="Orchestrator",
    )

    assert alert.is_critical is False
    assert alert.requires_action is False


def test_alert_severity_values():
    """
    Deve possuir todos os níveis esperados.
    """

    assert AlertSeverity.INFO.value == "INFO"
    assert AlertSeverity.WARNING.value == "WARNING"
    assert AlertSeverity.ERROR.value == "ERROR"
    assert AlertSeverity.CRITICAL.value == "CRITICAL"