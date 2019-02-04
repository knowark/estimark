from pytest import fixture
from estimark.infrastructure.resolver import Registry, Resolver
from estimark.infrastructure.config import build_config, Config
from estimark.infrastructure.factories import build_factory


@fixture
def trial_config() -> Config:
    return build_config(None, 'TEST')


@fixture
def trial_resolver(trial_config) -> Registry:
    config = trial_config
    factory = build_factory(config)
    strategy = config['strategy']
    resolver = Resolver(strategy=strategy, factory=factory)
    return resolver
