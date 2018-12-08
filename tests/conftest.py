from pytest import fixture
from estimark.infrastructure.resolver import Registry, Resolver
from estimark.infrastructure.config import build_config
from estimark.infrastructure.factories import build_factories


@fixture
def trial_registry() -> Registry:
    config = build_config(None, 'TEST')

    factories = build_factories(config)
    resolver = Resolver(config, factories)
    providers = config['providers']
    registry = resolver.resolve(providers)

    return registry
