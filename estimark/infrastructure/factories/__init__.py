from typing import Dict, Any
from .memory_factory import MemoryFactory
from .trial_factory import TrialFactory
from ..config import Config


def build_factories(config: Config) -> Dict[str, Any]:
    return {
        'MemoryFactory': MemoryFactory(config),
        'TrialFactory': TrialFactory(config)
    }
