from pathlib import Path
from json import load
from .config import Config
from .trial_config import TrialConfig


def build_config(config_path: str, mode: str) -> Config:
    return TrialConfig()


def load_config(config_path: str) -> Config:
    path = Path(config_path)
    if not path.exists():
        return None

    with open(config_path) as f:
        return load(f)
