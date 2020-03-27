from pytest import fixture
from injectark import Injectark
from estimark.infrastructure.config import build_config
from estimark.infrastructure.factories import build_factory, build_strategy


@fixture
def trial_config():
    return build_config('DEV')


@fixture
def trial_injector(trial_config) -> Injectark:
    config = trial_config
    factory = build_factory(config)
    strategy = build_strategy(config['strategies'], config['strategy'])
    injector = Injectark(strategy=strategy, factory=factory)
    return injector
