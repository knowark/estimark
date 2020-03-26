from typing import List, Dict, Any
from .altair import altair
from .base import base
from .check import check
from .json import json
from .rst import rst


STRATEGIES = {
    'base': base,
    'altair': altair,
    'check': check,
    'json': json,
    'rst': rst
}


def build_strategy(strategies: List[str],
                   custom_strategy: Dict[str, Any]={}) -> Dict[str, Any]:
    strategy: Dict[str, Any] = {}
    for name in strategies:
        strategy.update(STRATEGIES[name])
    strategy.update(custom_strategy)
    return strategy
