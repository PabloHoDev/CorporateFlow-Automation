def test_should_create_logger():

    service = LogService()

    logger = service.get_logger()

    assert logger is not None