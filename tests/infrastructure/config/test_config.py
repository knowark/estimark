from estimark.infrastructure.config import Config, load_config


def test_config_instantiation():
    class CustomConfig(Config):
        def __init__(self):
            super().__init__()

    assert CustomConfig().get('mode') == 'BASE'


def test_load_config_not_exits():
    result = load_config('NOT_EXISTING.json')
    assert result is None


def test_load_config(tmpdir):
    config_file = tmpdir.mkdir("config").join(
        "prod_config.json")
    config_file.write('{"mode": "PROD"}')

    result = load_config(str(config_file))

    assert result['mode'] == 'PROD'
