from typing import Dict, Any
from .memory_factory import MemoryFactory
from .altair_factory import AltairFactory
from .check_factory import CheckFactory
from .rst_factory import RstFactory
from .json_factory import JsonFactory
from ..config import Config
from .factory import Factory
from .strategies import build_strategy


def build_factory(config: Config) -> Factory:
    return {
        'AltairFactory': AltairFactory(config),
        'CheckFactory': CheckFactory(config),
        'JsonFactory': JsonFactory(config),
        'MemoryFactory': MemoryFactory(config),
        'RstFactory': RstFactory(config)
    }.get(config.get('factory', 'MemoryFactory'))
