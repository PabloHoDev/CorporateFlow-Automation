def test_should_generate_report():

    service = ReportService()

    results = [
        ProcessingResult(
            success=True
        )
    ]

    report = service.generate_report(
        results=results,
        started_at=datetime.now()
    )

    assert len(report.results) == 1