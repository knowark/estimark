from pytest import fixture
from injectark import Injectark
from estimark.core import DEVELOPMENT_CONFIG
from estimark.factories import factory_builder, strategy_builder
from estimark.presenters.shell import Shell

# @fixture
# def trial_config():
#     return build_config('DEV')


# @fixture
# def trial_injector(trial_config) -> Injectark:
#     config = DEVELOPMENT_CONFIG

#     strategy = strategy_builder.build(config['strategies'])
#     factory = factory_builder.build(config)
#     injector = Injectark(strategy, factory)

#     return injector


@fixture
def shell() -> Shell:
    config = DEVELOPMENT_CONFIG
    strategy = strategy_builder.build(config['strategies'])
    factory = factory_builder.build(config)

    injector = Injectark(strategy, factory)

    return Shell(config, injector)
