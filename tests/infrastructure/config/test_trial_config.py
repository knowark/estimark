from estimark.infrastructure.config import TrialConfig, build_config


def test_trial_config_instantiation():
    assert TrialConfig().get('mode') == 'TEST'
    assert TrialConfig().get('factory') == 'TrialFactory'


def test_build_config_trial():
    config = build_config(None, 'TEST')
    assert isinstance(config, TrialConfig)
