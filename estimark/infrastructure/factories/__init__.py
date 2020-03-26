from typing import Dict, Any
from .memory_factory import MemoryFactory
from .check_factory import CheckFactory
from .rst_factory import RstFactory
from .json_factory import JsonFactory
from ..config import Config
from .factory import Factory
from .strategies import build_strategy


def build_factory(config: Config) -> Factory:
    return {
        'RstFactory': RstFactory(config),
        'MemoryFactory': MemoryFactory(config),
        'CheckFactory': CheckFactory(config)
    }.get(config.get('factory', 'MemoryFactory'))
