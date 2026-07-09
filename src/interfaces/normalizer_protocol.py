from abc import ABC, abstractmethod
from typing import Any


class Normalizer(ABC):

    @abstractmethod
    def normalize(self, value: Any) -> Any:
        """
        Normalizes an input value and returns
        its normalized representation.
        """
        pass