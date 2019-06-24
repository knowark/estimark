from pytest import fixture
from injectark import Injectark
from estimark.infrastructure.config import build_config, Config
from estimark.infrastructure.factories import build_factory


@fixture
def trial_config() -> Config:
    return build_config(None, 'TEST')


@fixture
def trial_resolver(trial_config) -> Injectark:
    config = trial_config
    factory = build_factory(config)
    strategy = config['strategy']
    resolver = Injectark(strategy=strategy, factory=factory)
    return resolver
