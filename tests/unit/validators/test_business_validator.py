import pandas as pd
import pytest

from src.validators.business_validator import (
    BusinessValidator
)

from src.exceptions.business_rule_error import (
    BusinessRuleError
)


validator = BusinessValidator()