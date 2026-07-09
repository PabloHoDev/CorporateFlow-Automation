from abc import ABC, abstractmethod

from src.models.input_file import InputFile


class Validator(ABC):

    @abstractmethod
    def validate(self, input_file: InputFile) -> None:
        """
        Validates an input file.

        Raises:
            Validation exceptions when validation fails.
        """
        pass