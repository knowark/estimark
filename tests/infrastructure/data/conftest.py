from pytest import fixture
from estimark.infrastructure.data import RstAnalyzer


@fixture
def rst_file() -> str:
    with open('test_assets/rst_directory/index.rst') as f:
        return f.read()


@fixture
def rst_analyzer() -> str:
    return RstAnalyzer()
