from src.models.processing_result import ProcessingResult


def test_should_create_success_result():

    result = ProcessingResult(
        success=True,
        processed_records=100,
        skipped_records=5,
        failed_records=0,
        errors=[]
    )

    assert result.success is True
    assert result.processed_records == 100
    assert result.failed_records == 0