import pandas as pd

from src.exceptions.file_validation_error import (
    FileValidationError
)
from src.interfaces.validator import Validator


class SchemaValidator(Validator):

    REQUIRED_COLUMNS = {
        "USUARIO",
        "COD. PROCEDIMENTO"
        "PROCEDIMENTO",
        "NOME DO PRESTADOR",
        "UF PRESTADOR",
        "CIDADE PRESTADOR",
        "VALOR DEPOSITO",
        "DATA DEPOSITO",
        "OBRIGACAO",
        "AREA DA PENDENCIA",
        "STATUS"
    }

    def validate(
        self,
        dataframe: pd.DataFrame
    ) -> None:

        if dataframe.empty:
            raise FileValidationError(
                "Input file contains no records."
            )

        missing_columns = (
            self.REQUIRED_COLUMNS -
            set(dataframe.columns)
        )

        if missing_columns:
            raise FileValidationError(
                (
                    "Missing required columns: "
                    f"{missing_columns}"
                )
            )