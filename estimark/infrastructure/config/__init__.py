from pathlib import Path
from json import load
from .config import Config
from .trial_config import TrialConfig
from .production_config import ProductionConfig


def build_config(config_path: str, mode: str) -> Config:
    if mode != 'PROD':
        return TrialConfig()

    config = ProductionConfig()
    loaded_config = load_config(config_path)
    if loaded_config:
        config = update_config(config, loaded_config)

    return config


def load_config(config_path: str) -> Config:
    path = Path(config_path)
    if not path.exists():
        return None

    with open(config_path) as f:
        return load(f)


def update_config(base_config: ProductionConfig, overlay_config: Config
                  ) -> ProductionConfig:
    overlay_strategy = base_config.pop('strategy')
    base_config.update(overlay_config)
    base_config['strategy'].update(overlay_strategy)
    return base_config
