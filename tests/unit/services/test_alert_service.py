from src.models.alert import (
    Alert,
    AlertSeverity,
)
from src.services.alert_service import AlertService


def create_alert(
    severity: AlertSeverity = AlertSeverity.INFO,
) -> Alert:
    return Alert(
        title="Teste",
        message="Mensagem de teste",
        severity=severity,
        source="TestService",
    )


def test_register_alert():
    """
    Deve registrar um alerta.
    """

    service = AlertService()

    service.register(
        create_alert()
    )

    assert service.count() == 1


def test_get_all_alerts():
    """
    Deve retornar todos os alertas.
    """

    service = AlertService()

    service.register(create_alert())
    service.register(create_alert())

    alerts = service.get_all()

    assert len(alerts) == 2


def test_filter_by_severity():
    """
    Deve filtrar corretamente por severidade.
    """

    service = AlertService()

    service.register(
        create_alert(AlertSeverity.INFO)
    )

    service.register(
        create_alert(AlertSeverity.ERROR)
    )

    service.register(
        create_alert(AlertSeverity.ERROR)
    )

    errors = service.get_by_severity(
        AlertSeverity.ERROR
    )

    assert len(errors) == 2


def test_get_critical_alerts():
    """
    Deve retornar apenas alertas críticos.
    """

    service = AlertService()

    service.register(
        create_alert(AlertSeverity.CRITICAL)
    )

    service.register(
        create_alert(AlertSeverity.WARNING)
    )

    criticals = service.get_critical_alerts()

    assert len(criticals) == 1

    assert (
        criticals[0].severity
        == AlertSeverity.CRITICAL
    )


def test_count_by_severity():
    """
    Deve contar corretamente por severidade.
    """

    service = AlertService()

    service.register(
        create_alert(AlertSeverity.ERROR)
    )

    service.register(
        create_alert(AlertSeverity.ERROR)
    )

    service.register(
        create_alert(AlertSeverity.WARNING)
    )

    assert (
        service.count_by_severity(
            AlertSeverity.ERROR
        ) == 2
    )

    assert (
        service.count_by_severity(
            AlertSeverity.WARNING
        ) == 1
    )


def test_has_critical_alerts():
    """
    Deve identificar presença de alertas críticos.
    """

    service = AlertService()

    assert (
        service.has_critical_alerts()
        is False
    )

    service.register(
        create_alert(
            AlertSeverity.CRITICAL
        )
    )

    assert (
        service.has_critical_alerts()
        is True
    )


def test_clear_alerts():
    """
    Deve remover todos os alertas.
    """

    service = AlertService()

    service.register(create_alert())
    service.register(create_alert())

    assert service.count() == 2

    service.clear()

    assert service.count() == 0


def test_get_all_returns_copy():
    """
    Deve retornar uma cópia da lista interna.
    """

    service = AlertService()

    service.register(create_alert())

    alerts = service.get_all()

    alerts.clear()

    assert service.count() == 1