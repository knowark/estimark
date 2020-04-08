from pytest import fixture, raises
from estimark.infrastructure.config import build_config
from estimark.infrastructure.cli import Cli


@fixture
def cli(trial_config, trial_injector):
    cli = Cli(trial_config, trial_injector)
    return cli


def test_cli_initialization(cli):
    assert cli is not None


def test_cli_parse_no_arguments(cli):
    with raises(SystemExit):
        result = cli.parse([])


def test_cli_parse_estimate(cli):
    arg_list = ['estimate']
    namespace = cli.parse(arg_list)
    assert namespace.action == 'estimate'


def test_cli_parse_show(cli):
    arg_list = ['show']
    namespace = cli.parse(arg_list)
    assert namespace.action == 'show'


def test_cli_run(cli):
    test_dict = {
        'call_dict': None
    }

    def mock_parse(args):
        class MockNamespace:
            def __init__(self):
                self.field = 'value'

            def func(self, options_dict):
                test_dict['call_dict'] = options_dict
        return MockNamespace()

    cli.parse = mock_parse

    args = ['estimate']

    cli.run(args)

    assert isinstance(test_dict['call_dict'], dict)
    assert test_dict['call_dict'] == {'field': 'value'}


def test_cli_estimate(cli):
    options_dict = {}
    assert cli.estimate(options_dict) is None


def test_cli_show(cli):
    options_dict = {'model': 'task'}
    assert cli.show(options_dict) is None


def test_cli_show_unknown(cli):
    options_dict = {'model': 'unknown'}
    with raises(ValueError):
        cli.show(options_dict)


def test_cli_version(cli):
    options_dict = {}
    assert cli.version(options_dict) is None


def test_cli_plot(cli):
    options_dict = {'type': 'kanban',
                    'context': '{}'}
    assert cli.plot(options_dict) is None
