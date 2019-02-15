import os
from json import dump
from typing import Dict, Any


def init_json_database(path: str, schema: Dict[str, Any]) -> bool:
    if os.path.exists(path):
        return False
    with open(path, 'w') as f:
        dump(schema, f)  # type: ignore
    return True
