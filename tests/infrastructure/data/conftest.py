import os
from pytest import fixture
from estimark.infrastructure.data import RstAnalyzer


@fixture
def rst_file() -> str:
    data_path = os.path.dirname(__file__)

    with open(os.path.join(
            data_path, 'test_assets/rst_directory/index.rst')) as f:
        return f.read()


@fixture
def rst_analyzer() -> str:
    return RstAnalyzer()
