import logging
from pathlib import Path


LOG_DIRECTORY = Path("logs")
LOG_FILE = LOG_DIRECTORY / "corporateflow.log"


def setup_logger(
    name: str = "CorporateFlow",
    level: int = logging.INFO
) -> logging.Logger:

    """
    Configura e retorna o logger principal da aplicação.

    Parameters
    ----------
    name:
        Nome do logger.

    level:
        Nível mínimo de log.

    Returns
    -------
    logging.Logger
        Logger configurado.
    """

    logger = logging.getLogger(name)

    logger.setLevel(level)

    if logger.handlers:
        return logger


    LOG_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True
    )


    formatter = logging.Formatter(
        fmt=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S"
    )


    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)


    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)


    logger.addHandler(file_handler)

    logger.addHandler(console_handler)


    return logger