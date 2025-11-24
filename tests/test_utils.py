import json

from src.utils.utils import read_json


def test_read_json_valid(tmp_path):
    file = tmp_path / "data.json"
    data = [{"id": 1}]
    file.write_text(json.dumps(data), encoding="utf-8")

    assert read_json(str(file)) == data


def test_read_json_not_list(tmp_path):
    file = tmp_path / "data.json"
    file.write_text(json.dumps({"id": 1}), encoding="utf-8")

    assert read_json(str(file)) == []


def test_read_json_missing_file():
    assert read_json("no_file.json") == []
