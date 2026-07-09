from src.core.execution_context import ExecutionContext
from src.models.app_config import AppConfig


class Orchestrator:

    def __init__(
        self,
        app_config: AppConfig,
        file_service,
        backup_service,
        excel_service,
        report_service,
        schema_validator,
        business_validator,
        text_normalizer,
        city_normalizer
    ):
        self.app_config = app_config

        self.file_service = file_service
        self.backup_service = backup_service
        self.excel_service = excel_service
        self.report_service = report_service

        self.schema_validator = schema_validator
        self.business_validator = business_validator

        self.text_normalizer = text_normalizer
        self.city_normalizer = city_normalizer