from pytest import fixture
from injectark import Injectark
from estimark.core import config
from estimark.factories import factory_builder
from estimark.presenters.shell import Shell


@fixture
def shell() -> Shell:
    config['factory'] = 'CheckFactory'
    factory = factory_builder.build(config)

    injector = Injectark(factory)

    return Shell(config, injector)
