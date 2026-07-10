import pandas as pd
import pytest

from src.validators.schema_validator import SchemaValidator
from src.exceptions.file_validation_error import (
    FileValidationError
)


validator = SchemaValidator()