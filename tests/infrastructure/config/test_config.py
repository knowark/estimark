from estimark.infrastructure.config import (
    Config, load_config, update_config, build_config)
from estimark.infrastructure.config.production_config import ProductionConfig
from estimark.infrastructure.config.trial_config import TrialConfig


def test_config_instantiation():
    class CustomConfig(Config):
        def __init__(self):
            super().__init__()

    assert CustomConfig().get('mode') == 'BASE'


def test_load_config_not_exits():
    result = load_config('NOT_EXISTING.json')
    assert result is None


def test_load_config(tmpdir):
    config_file = tmpdir.mkdir("config").join(
        "prod_config.json")
    config_file.write('{"mode": "PROD"}')

    result = load_config(str(config_file))

    assert result['mode'] == 'PROD'


def test_update_config():
    base_config = {
        'mode': 'PROD',
        'factory': 'RstFactory',
        'strategy': {
            "RstAnalyzer": {
                "method": "rst_analyzer"
            },
            "TaskRepository": {
                "method": "rst_task_repository"
            }
        }
    }
    overlay_config = {
        'factory': 'TrialFactory',
        'strategy': {
            "TaskRepository": {
                "method": "memory_task_repository"
            }
        }
    }
    new_config = update_config(base_config, overlay_config)
    assert new_config['mode'] == 'PROD'
    assert new_config['factory'] == 'TrialFactory'
    assert new_config['strategy']['RstAnalyzer']['method'] == 'rst_analyzer'
    assert new_config[
        'strategy']['TaskRepository']['method'] == 'memory_task_repository'


def test_build_config(tmpdir):
    config_file = tmpdir.mkdir("config").join(
        "prod_config.json")
    config_file.write('{"mode": "PROD"}')

    config = build_config(str(config_file), 'PROD')
    assert isinstance(config, ProductionConfig)
