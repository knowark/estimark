import inspect
from pytest import fixture
from injectark import Injectark
from estimark.infrastructure.config import build_config
from estimark.infrastructure.factories import build_strategy, build_factory
from estimark.infrastructure.factories import altair_factory


@fixture
def mock_config():
    config = build_config('DEV')
    config['factory'] = 'AltairFactory'
    return config


@fixture
def mock_strategy(mock_config):
    strategy = build_strategy(['base', 'altair'])
    return strategy


def test_altair_factory(mock_config, mock_strategy, monkeypatch):
    factory = build_factory(mock_config)
    resolver = Injectark(strategy=mock_strategy, factory=factory)
    for resource in mock_strategy.keys():
        result = resolver.resolve(resource)
        classes = inspect.getmro(type(result))
        assert resource in [item.__name__ for item in classes]
