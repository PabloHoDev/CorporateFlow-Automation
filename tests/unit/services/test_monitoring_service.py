from src.models.execution_metrics import ExecutionMetrics
from src.services.monitoring_service import MonitoringService


def create_metrics(
    execution_time: float = 100,
    errors: int = 0
) -> ExecutionMetrics:
    """
    Cria métricas para testes.
    """

    metrics = ExecutionMetrics()

    metrics.files_processed = 2
    metrics.records_read = 1000
    metrics.records_created = 100
    metrics.records_updated = 50
    metrics.records_skipped = 850
    metrics.errors_count = errors

    metrics.finish()

    metrics.start_time = (
        metrics.end_time
        .replace()
    )

    metrics.end_time = (
        metrics.start_time
        .replace()
    )

    metrics.end_time = (
        metrics.start_time
        + __import__("datetime").timedelta(
            seconds=execution_time
        )
    )

    return metrics


def test_register_execution():
    """
    Deve registrar uma execução.
    """

    service = MonitoringService()

    metrics = create_metrics()

    snapshot = service.register_execution(
        metrics
    )

    assert snapshot.records_read == 1000

    assert (
        service.get_total_executions()
        == 1
    )


def test_total_executions():
    """
    Deve contar corretamente as execuções.
    """

    service = MonitoringService()

    service.register_execution(
        create_metrics()
    )

    service.register_execution(
        create_metrics()
    )

    service.register_execution(
        create_metrics()
    )

    assert (
        service.get_total_executions()
        == 3
    )


def test_success_rate():
    """
    Deve calcular corretamente
    a taxa de sucesso.
    """

    service = MonitoringService()

    service.register_execution(
        create_metrics(errors=0)
    )

    service.register_execution(
        create_metrics(errors=0)
    )

    service.register_execution(
        create_metrics(errors=1)
    )

    assert (
        service.get_success_rate()
        == (2 / 3)
    )


def test_average_execution_time():
    """
    Deve calcular o tempo médio.
    """

    service = MonitoringService()

    service.register_execution(
        create_metrics(
            execution_time=100
        )
    )

    service.register_execution(
        create_metrics(
            execution_time=200
        )
    )

    assert (
        service.get_average_execution_time()
        == 150
    )


def test_empty_service():
    """
    Deve retornar zero
    quando não houver execuções.
    """

    service = MonitoringService()

    assert (
        service.get_total_executions()
        == 0
    )

    assert (
        service.get_success_rate()
        == 0.0
    )

    assert (
        service.get_average_execution_time()
        == 0.0
    )


def test_snapshots_property():
    """
    Deve retornar cópia da lista.
    """

    service = MonitoringService()

    service.register_execution(
        create_metrics()
    )

    snapshots = service.snapshots

    assert len(snapshots) == 1

    snapshots.clear()

    assert (
        service.get_total_executions()
        == 1
    )