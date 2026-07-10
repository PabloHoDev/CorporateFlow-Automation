import pytest

from src.exceptions.configuration_error import (
    ConfigurationError
)


def test_should_raise_configuration_error():

    with pytest.raises(ConfigurationError):
        raise ConfigurationError(
            "Configuration file not found."
        )