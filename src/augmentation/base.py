from abc import ABCMeta, abstractmethod
from typing import Any


class BaseAugmentation(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def apply(self, input_image: Any, params: dict[str, Any]) -> Any:
        raise NotImplementedError()
