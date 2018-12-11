from pytest import fixture
from estimark.infrastructure.resolver import Registry, Resolver
from estimark.infrastructure.config import build_config, Config
from estimark.infrastructure.factories import build_factories


@fixture
def trial_config() -> Config:
    return build_config(None, 'TEST')


@fixture
def trial_registry(trial_config) -> Registry:
    config = trial_config
    factories = build_factories(config)
    resolver = Resolver(config, factories)
    providers = config['providers']
    registry = resolver.resolve(providers)

    return registry
