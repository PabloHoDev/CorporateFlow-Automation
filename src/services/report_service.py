from datetime import datetime

from src.interfaces.service import Service
from src.models.processing_result import ProcessingResult
from src.models.report import Report


class ReportService(Service):

    def generate_report(
        self,
        results: list[ProcessingResult],
        started_at: datetime
    ) -> Report:

        return Report(
            started_at=started_at,
            finished_at=datetime.now(),
            results=results
        )