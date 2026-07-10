import pytest

from src.exceptions.file_validation_error import (
    FileValidationError
)


def test_should_raise_file_validation_error():

    with pytest.raises(FileValidationError):
        raise FileValidationError(
            "Missing required columns."
        )