from pytest import raises
from estimark.presenters.shell import shell as shell_module


def test_shell_initialization(shell):
    assert shell is not None


def test_shell_parse_no_arguments(shell):
    with raises(SystemExit):
        result = shell.parse([])


def test_shell_parse_estimate(shell):
    arg_list = ['estimate']
    namespace = shell.parse(arg_list)
    assert namespace.action == 'estimate'


def test_shell_parse_show(shell):
    arg_list = ['show']
    namespace = shell.parse(arg_list)
    assert namespace.action == 'show'


def test_shell_run(shell):
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

    shell.parse = mock_parse

    args = ['estimate']

    shell.run(args)

    assert isinstance(test_dict['call_dict'], dict)
    assert test_dict['call_dict'] == {'field': 'value'}


def test_shell_init(shell):
    options_dict = {}
    assert shell.init(options_dict) is None


def test_shell_estimate(shell):
    options_dict = {}
    assert shell.estimate(options_dict) is None


def test_shell_estimate_states(shell):
    options_dict = {"states": "backlog, open"}
    assert shell.estimate(options_dict) is None


def test_shell_show(shell):
    options_dict = {'model': 'task'}
    assert shell.show(options_dict) is None


def test_shell_show_unknown(shell):
    options_dict = {'model': 'unknown'}
    with raises(ValueError):
        shell.show(options_dict)


def test_shell_version(shell):
    options_dict = {}
    assert shell.version(options_dict) is None


def test_shell_plot(shell):
    options_dict = {'type': 'kanban',
                    'context': '{}'}
    assert shell.plot(options_dict) is None
