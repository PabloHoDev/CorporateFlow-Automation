from src.normalizers.city_normalizer import (
    CityNormalizer
)

from src.normalizers.text_normalizer import (
    TextNormalizer
)

normalizer = CityNormalizer(
    TextNormalizer()
)