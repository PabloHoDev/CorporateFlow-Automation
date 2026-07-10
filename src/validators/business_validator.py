import pandas as pd

from src.exceptions.business_rule_error import (
    BusinessRuleError
)
from src.interfaces.validator import Validator


class BusinessValidator(Validator):

    VALID_UFS = {
        "AC", "AL", "AP", "AM", "BA",
        "CE", "DF", "ES", "GO", "MA",
        "MT", "MS", "MG", "PA", "PB",
        "PR", "PE", "PI", "RJ", "RN",
        "RS", "RO", "RR", "SC", "SP",
        "SE", "TO"
    }

    VALID_STATUS = {
        "PENDENTE",
        "NEGADO"
    }

    VALID_AREAS = {
        "RELACIONAMENTO",
        "ASSIST RELACIONAMENTO",
        "FINAN ATENDIMENTO",
        "AUD AUTORIZACAO"
    }

    def validate(
        self,
        dataframe: pd.DataFrame
    ) -> None:

        invalid_ufs = (
            dataframe[
                ~dataframe["UF PRESTADOR"]
                .isin(self.VALID_UFS)
            ]
        )

        if not invalid_ufs.empty:
            raise BusinessRuleError(
                "Invalid UF detected."
            )

        invalid_status = (
            dataframe[
                ~dataframe["STATUS"]
                .isin(self.VALID_STATUS)
            ]
        )

        if not invalid_status.empty:
            raise BusinessRuleError(
                "Invalid status detected."
            )