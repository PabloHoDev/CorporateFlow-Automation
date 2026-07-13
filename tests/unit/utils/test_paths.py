class Paths:
    @staticmethod
    def build_input_path(filename: str) -> Path:
        ...
#exemplo de teste


from pathlib import Path

from src.utils.paths import Paths


def test_should_build_input_path():

    result = Paths.build_input_path(
        "arquivo.xlsx"
    )

    assert result == Path(
        "input/arquivo.xlsx"
    )


def test_should_build_output_path():

    result = Paths.build_output_path(
        "resultado.xlsx"
    )

    assert result == Path(
        "output/resultado.xlsx"
    )