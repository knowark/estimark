from pathlib import Path
from json import load
from .config import Config, DevelopmentConfig, ProductionConfig


def build_config(mode: str, config_path: str = "") -> Config:
    if mode != 'PROD':
        return DevelopmentConfig()

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
    overlay_strategy = None
    if 'strategy' in overlay_config:
        overlay_strategy = overlay_config.pop('strategy')
    base_config.update(overlay_config)
    if overlay_strategy:
        base_config['strategy'].update(overlay_strategy)

    return base_config
