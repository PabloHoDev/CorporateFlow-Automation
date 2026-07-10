import re
import unicodedata

from src.interfaces.normalizer import Normalizer


class TextNormalizer(Normalizer):

    def normalize(
        self,
        value: str | None
    ) -> str:

        if value is None:
            return ""

        value = str(value)

        value = value.strip()

        value = unicodedata.normalize(
            "NFKD",
            value
        ).encode(
            "ASCII",
            "ignore"
        ).decode(
            "ASCII"
        )

        value = value.upper()

        value = re.sub(
            r"\s+",
            " ",
            value
        )

        return value