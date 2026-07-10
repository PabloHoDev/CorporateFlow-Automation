import pytest

from src.exceptions.business_rule_error import (
    BusinessRuleError
)


def test_should_raise_business_rule_error():

    with pytest.raises(BusinessRuleError):
        raise BusinessRuleError(
            "Invalid UF."
        )