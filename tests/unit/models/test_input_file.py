from datetime import datetime
from pathlib import Path

from src.models.input_file import InputFile


def test_should_create_input_file():

    file = InputFile(
        file_name="clientes.xlsx",
        stem="clientes",
        extension=".xlsx",
        path=Path("./input/clientes.xlsx"),
        size_bytes=1000,
        created_at=datetime.now(),
        modified_at=datetime.now(),
        discovered_at=datetime.now()
    )

    assert file.file_name == "clientes.xlsx"
    assert file.extension == ".xlsx"
    assert file.size_bytes == 1000