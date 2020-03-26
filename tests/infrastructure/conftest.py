from pytest import fixture
from injectark import Injectark
from estimark.infrastructure.config import build_config
from estimark.infrastructure.factories import build_factory, build_strategy


@fixture
def trial_config():
    return build_config('TEST')


@fixture
def trial_resolver(trial_config) -> Injectark:
    config = trial_config
    factory = build_factory(config)
    strategy = build_strategy(config['strategies'], config['strategy'])
    resolver = Injectark(strategy=strategy, factory=factory)
    return resolver
