from json import load, dump
from pathlib import Path
from pytest import fixture
from typing import Dict, Any
from estimark.infrastructure.core.setup import json_setup_supplier
from estimark.infrastructure.core import JsonSetupSupplier


def test_json_setup_supplier_setup(tmpdir):
    database_schema = {
        'schedules': {},
        'slots': {}
    }

    file_path = str(tmpdir.mkdir("estimark").join('estimark_data.json'))
    setup_supplier = JsonSetupSupplier(file_path, database_schema)
    setup_supplier.setup()

    data = {}
    with open(file_path) as f:
        data = load(f)

    assert 'schedules' in data
    assert 'slots' in data


def test_json_setup_supplier_setup_with_existing_file(tmpdir):
    file_path = str(tmpdir.mkdir("estimark").join('estimark_data.json'))
    database_schema = {
        'schedules': {},
        'slots': {}
    }

    with open(file_path, 'w') as f:
        dump({}, f)

    setup_supplier = JsonSetupSupplier(file_path, database_schema)
    setup_supplier.setup()

    with open(file_path) as f:
        data = load(f)

    assert 'schedules' not in data
    assert 'slots' not in data
