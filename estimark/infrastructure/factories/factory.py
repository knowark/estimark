from abc import ABC, abstractmethod
from typing import Dict, Any


class Factory(ABC):
    @abstractmethod
    def __init__(self, config: Dict[str, Any]) -> None:
        pass
