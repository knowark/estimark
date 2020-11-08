from pytest import fixture
from injectark import Injectark
from estimark.core import config
from estimark.factories import factory_builder, strategy_builder
from estimark.presenters.shell import Shell


@fixture
def shell() -> Shell:
    config['factory'] = 'CheckFactory'
    config['strategies'] = ['base', 'check']

    strategy = strategy_builder.build(config['strategies'])
    factory = factory_builder.build(config)

    injector = Injectark(strategy, factory)

    return Shell(config, injector)
