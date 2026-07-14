import logging

from src.utils.logger import setup_logger


def test_logger_creation(tmp_path, monkeypatch):
    """
    Deve criar um logger configurado corretamente.
    """

    log_directory = tmp_path / "logs"
    log_file = log_directory / "test.log"


    monkeypatch.setattr(
        "src.utils.logger.LOG_DIRECTORY",
        log_directory
    )

    monkeypatch.setattr(
        "src.utils.logger.LOG_FILE",
        log_file
    )


    logger = setup_logger(
        name="TestLogger"
    )


    assert isinstance(
        logger,
        logging.Logger
    )


    assert logger.name == "TestLogger"


def test_logger_writes_file(tmp_path, monkeypatch):
    """
    Deve escrever mensagens no arquivo de log.
    """

    log_directory = tmp_path / "logs"
    log_file = log_directory / "test.log"


    monkeypatch.setattr(
        "src.utils.logger.LOG_DIRECTORY",
        log_directory
    )

    monkeypatch.setattr(
        "src.utils.logger.LOG_FILE",
        log_file
    )


    logger = setup_logger(
        name="FileLogger"
    )


    logger.info(
        "Teste de escrita"
    )


    assert log_file.exists()


    content = log_file.read_text(
        encoding="utf-8"
    )


    assert "Teste de escrita" in content


def test_logger_does_not_duplicate_handlers():
    """
    Não deve adicionar handlers duplicados
    quando chamado várias vezes.
    """

    logger_one = setup_logger(
        name="DuplicateLogger"
    )


    handlers_before = len(
        logger_one.handlers
    )


    logger_two = setup_logger(
        name="DuplicateLogger"
    )


    handlers_after = len(
        logger_two.handlers
    )


    assert handlers_before == handlers_after