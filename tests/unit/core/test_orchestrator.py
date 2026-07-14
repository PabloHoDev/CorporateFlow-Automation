from unittest.mock import Mock

from src.core.orchestrator import (
    Orchestrator
)


def test_should_execute_pipeline():

    file_service = Mock()
    backup_service = Mock()
    excel_service = Mock()
    report_service = Mock()

    schema_validator = Mock()
    business_validator = Mock()

    text_normalizer = Mock()
    city_normalizer = Mock()

    orchestrator = Orchestrator(
        file_service=file_service,
        backup_service=backup_service,
        excel_service=excel_service,
        report_service=report_service,
        schema_validator=schema_validator,
        business_validator=business_validator,
        text_normalizer=text_normalizer,
        city_normalizer=city_normalizer
    )

    orchestrator.run()

    file_service.list_files.assert_called()