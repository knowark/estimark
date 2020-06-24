from json import load, dump
from estimark.core.data.json import init_json_database


def test_init_json_database(tmpdir):
    database_schema = {
        'schedules': {},
        'slots': {}
    }

    file_path = str(tmpdir.mkdir("estimark").join('estimark_data.json'))
    result = init_json_database(file_path, database_schema)

    data = {}
    with open(file_path) as f:
        data = load(f)

    assert 'schedules' in data
    assert 'slots' in data
    assert result is True


def test_init_json_database_existing_file(tmpdir):
    file_path = str(tmpdir.mkdir("estimark").join('estimark_data.json'))
    database_schema = {
        'schedules': {},
        'slots': {}
    }

    with open(file_path, 'w') as f:
        dump({}, f)

    result = init_json_database(file_path, database_schema)
    assert result is False
