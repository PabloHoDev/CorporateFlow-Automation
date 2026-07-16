from datetime import datetime

from src.models.monitoring_snapshot import MonitoringSnapshot


def test_snapshot_creation():
    """
    Deve criar um MonitoringSnapshot corretamente.
    """

    snapshot = MonitoringSnapshot(
        timestamp=datetime.now(),
        execution_time_seconds=120,
        files_processed=2,
        records_read=1000,
        records_created=100,
        records_updated=50,
        records_skipped=850,
        errors_count=0,
    )

    assert snapshot.files_processed == 2
    assert snapshot.records_read == 1000
    assert snapshot.records_created == 100
    assert snapshot.records_updated == 50
    assert snapshot.records_skipped == 850
    assert snapshot.errors_count == 0


def test_success_when_no_errors():
    """
    Deve indicar sucesso quando não houver erros.
    """

    snapshot = MonitoringSnapshot(
        timestamp=datetime.now(),
        execution_time_seconds=100,
        files_processed=1,
        records_read=100,
        records_created=10,
        records_updated=5,
        records_skipped=85,
        errors_count=0,
    )

    assert snapshot.success is True


def test_failure_when_errors_exist():
    """
    Deve indicar falha quando houver erros.
    """

    snapshot = MonitoringSnapshot(
        timestamp=datetime.now(),
        execution_time_seconds=100,
        files_processed=1,
        records_read=100,
        records_created=10,
        records_updated=5,
        records_skipped=85,
        errors_count=2,
    )

    assert snapshot.success is False


def test_processed_records_calculation():
    """
    Deve calcular corretamente os registros processados.
    """

    snapshot = MonitoringSnapshot(
        timestamp=datetime.now(),
        execution_time_seconds=100,
        files_processed=1,
        records_read=1000,
        records_created=120,
        records_updated=30,
        records_skipped=850,
        errors_count=0,
    )

    assert snapshot.processed_records == 1000


def test_throughput_calculation():
    """
    Deve calcular corretamente os registros por segundo.
    """

    snapshot = MonitoringSnapshot(
        timestamp=datetime.now(),
        execution_time_seconds=100,
        files_processed=1,
        records_read=1000,
        records_created=100,
        records_updated=100,
        records_skipped=800,
        errors_count=0,
    )

    assert snapshot.throughput == 10.0


def test_throughput_with_zero_execution_time():
    """
    Deve retornar zero quando o tempo de execução for zero.
    """

    snapshot = MonitoringSnapshot(
        timestamp=datetime.now(),
        execution_time_seconds=0,
        files_processed=1,
        records_read=100,
        records_created=10,
        records_updated=10,
        records_skipped=80,
        errors_count=0,
    )

    assert snapshot.throughput == 0.0