from typing import Dict, Any
from .standard_factory import StandardFactory
from .trial_factory import TrialFactory
from .rst_factory import RstFactory
from ..config import Config
from .factory import Factory


def build_factory(config: Config) -> Factory:
    return {
        'RstFactory': RstFactory(config),
        'StandardFactory': StandardFactory(config),
        'TrialFactory': TrialFactory(config)
    }.get(config.get('factory', 'StandardFactory'))
