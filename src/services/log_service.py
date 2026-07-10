import logging

from src.interfaces.service import Service


class LogService(Service):

    def get_logger(
        self,
        name: str
    ) -> logging.Logger:

        return logging.getLogger(name)