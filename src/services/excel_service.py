from pathlib import Path

import pandas as pd

from src.interfaces.service import Service


class ExcelService(Service):

    def read_excel(
        self,
        file_path: Path,
        **kwargs
    ) -> pd.DataFrame:
        """
        Reads an Excel file and returns a DataFrame.
        """

        return pd.read_excel(
            file_path,
            **kwargs
        )

    def read_csv(
        self,
        file_path: Path,
        **kwargs
    ) -> pd.DataFrame:
        """
        Reads a CSV file and returns a DataFrame.
        """

        return pd.read_csv(
            file_path,
            **kwargs
        )

    def write_excel(
        self,
        dataframe: pd.DataFrame,
        output_path: Path,
        **kwargs
    ) -> None:
        """
        Writes a DataFrame to an Excel file.
        """

        dataframe.to_excel(
            output_path,
            index=False,
            **kwargs
        )

    def append_rows(
        self,
        dataframe: pd.DataFrame,
        rows: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Appends rows to a dataframe.
        """

        return pd.concat(
            [dataframe, rows],
            ignore_index=True
        )