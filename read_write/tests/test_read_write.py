import pytest

import os
from pathlib import Path
from reytools.read_write import read_yaml
from reytools.read_write import read_json


def test_read_yaml():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = Path(os.path.join(cur_dir, "files", "yaml_file.yaml"))
    data = read_yaml(data_path)
    assert data.INCLUDE_TOP == False
    assert data.EPOCHS == 1


def test_read_json():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = Path(os.path.join(cur_dir, "files", "json_file.json"))
    data = read_json(data_path)
    assert data.INCLUDE_TOP == False
    assert data.EPOCHS == 1
