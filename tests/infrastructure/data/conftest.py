import os
from pathlib import Path
from pytest import fixture
from estimark.infrastructure.data import RstAnalyzer


@fixture
def rst_file() -> str:
    data_path = os.path.dirname(__file__)

    with open(os.path.join(
            data_path, 'test_assets/sample-task.rst')) as f:
        return f.read()


@fixture
def rst_analyzer() -> str:
    return RstAnalyzer()


@fixture
def root_directory() -> str:
    return str(Path(__file__).parent.joinpath(
        'test_assets/requirements/project'))
