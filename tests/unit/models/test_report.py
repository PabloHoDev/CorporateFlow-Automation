def test_should_calculate_total_files():

    report = Report(
        started_at=datetime.now(),
        finished_at=datetime.now(),
        results=[
            ProcessingResult(success=True),
            ProcessingResult(success=False)
        ]
    )

    assert report.total_files == 2