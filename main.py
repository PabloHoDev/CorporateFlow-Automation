from pathlib import Path
from src.config.configuration_manager import ConfigurationManager
from src.core.orchestrator import Orchestrator
from src.services.file_service import FileService
from src.services.backup_service import BackupService
from src.services.log_service import LogService

from src.services.excel_service import ExcelService
from src.services.report_service import ReportService
from src.validators.schema_validator import SchemaValidator
from src.validators.business_validator import BusinessValidator

from src.normalizers.text_normalizer import TextNormalizer
from src.normalizers.city_normalizer import CityNormalizer


def main():
    

    configuration_manager = ConfigurationManager(
        Path("config/config.yaml")
    )

    app_config = configuration_manager.load()

    file_service = FileService()

    backup_service = BackupService()

    log_service = LogService()

    excel_service = ExcelService()

    report_service = ReportService()

    schema_validator = SchemaValidator()

    business_validator = BusinessValidator()

    text_normalizer = TextNormalizer()

    city_normalizer = CityNormalizer(
        text_normalizer
    )

    orchestrator = Orchestrator(
        app_config=app_config,

        file_service=file_service,
        backup_service=backup_service,
        excel_service=excel_service,
        report_service=report_service,

        schema_validator=schema_validator,
        business_validator=business_validator,

        text_normalizer=text_normalizer,
        city_normalizer=city_normalizer
    )

    report = orchestrator.run()

    print(
        f"""
Execution completed.

Files processed: {report.total_files}
Successful: {report.successful_files}
Failed: {report.failed_files}

Success rate:
{report.success_rate:.2f}%
"""
    )


if __name__ == "__main__":
    main()