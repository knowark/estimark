from pytest import fixture
from estimark.application.repositories import ExpressionParser
from estimark.infrastructure.data import RstAnalyzer, RstTaskRepository
from estimark.infrastructure.factories import RstFactory


@fixture
def rst_factory():
    config = {}
    return RstFactory(config)


def test_rst_factory_rst_analyzer(rst_factory):
    analyzer = rst_factory.rst_analyzer()
    assert isinstance(analyzer, RstAnalyzer)


def test_rst_factory_rst_task_repository(rst_factory):
    parser = ExpressionParser()
    analyzer = RstAnalyzer()
    repository = rst_factory.rst_task_repository(parser, analyzer)
    assert isinstance(repository, RstTaskRepository)
