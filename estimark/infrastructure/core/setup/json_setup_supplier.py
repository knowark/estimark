import os
from typing import Dict, Any
from json import dump
from pathlib import Path
from .setup_supplier import SetupSupplier
from .memory_setup_supplier import MemorySetupSupplier


DEFAULT_SCHEMA = {
    "schedules": {},
    "slots": {}
}


class JsonSetupSupplier(SetupSupplier):

    def __init__(self, path: str,
                 schema: Dict[str, Any] = DEFAULT_SCHEMA) -> None:
        self.path = path
        self.schema = schema

    def setup(self) -> None:
        if os.path.exists(self.path):
            return
        with open(self.path, 'w') as f:
            dump(self.schema, f)  # type: ignore
