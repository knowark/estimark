from pytest import fixture
from estimark.infrastructure.config import build_config
from estimark.infrastructure.cli import Cli


@fixture
def cli(trial_config, trial_registry):
    cli = Cli(trial_config, trial_registry)
    return cli


def test_cli_initialization(cli):
    assert cli is not None
