import re

from src.interfaces.normalizer import Normalizer
from src.normalizers.text_normalizer import (
    TextNormalizer
)


class CityNormalizer(Normalizer):

    def __init__(
        self,
        text_normalizer: TextNormalizer
    ):
        self._text_normalizer = (
            text_normalizer
        )

    def normalize(
        self,
        city: str | None
    ) -> str:

        normalized = (
            self._text_normalizer
            .normalize(city)
        )

        normalized = re.sub(
            r"\s*[-/]\s*[A-Z]{2}$",
            "",
            normalized
        )

        return normalized.strip()