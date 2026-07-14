from datetime import datetime, timedelta

from src.models.execution_metrics import ExecutionMetrics


def test_execution_metrics_creation():
    """
    Deve criar métricas com valores iniciais corretos.
    """

    metrics = ExecutionMetrics()


    assert isinstance(
        metrics.start_time,
        datetime
    )

    assert metrics.end_time is None

    assert metrics.files_processed == 0

    assert metrics.records_read == 0

    assert metrics.records_created == 0

    assert metrics.records_updated == 0

    assert metrics.records_skipped == 0

    assert metrics.errors_count == 0



def test_execution_metrics_finish():
    """
    Deve registrar o fim da execução.
    """

    metrics = ExecutionMetrics()


    metrics.finish()


    assert metrics.end_time is not None

    assert isinstance(
        metrics.end_time,
        datetime
    )



def test_execution_time_seconds():
    """
    Deve calcular corretamente o tempo de execução.
    """

    metrics = ExecutionMetrics()


    metrics.start_time = (
        datetime.now()
        - timedelta(seconds=10)
    )


    metrics.finish()


    assert (
        metrics.execution_time_seconds >= 10
    )



def test_execution_metrics_counters():
    """
    Deve permitir atualizar os contadores.
    """

    metrics = ExecutionMetrics()


    metrics.files_processed = 3

    metrics.records_read = 1000

    metrics.records_created = 200

    metrics.records_updated = 50

    metrics.records_skipped = 750


    assert metrics.files_processed == 3

    assert metrics.records_read == 1000

    assert metrics.records_created == 200

    assert metrics.records_updated == 50

    assert metrics.records_skipped == 750