import os
from unittest.mock import patch

from src.utils import get_transactions_from_json


def test_get_transactions_from_json(data_dir):
    file_path = os.path.join(data_dir, "operations.json")
    transactions_obj = get_transactions_from_json(file_path)
    assert type(transactions_obj) is list


def test_get_transactions_from_json_invalid_file(data_dir):
    file_path = os.path.join(data_dir, "abcdef.json")
    transactions_obj = get_transactions_from_json(file_path)
    assert transactions_obj == []


def test_get_transactions_from_json_invalid_data():
    fake_data = "abcd"
    with patch("json.load", return_value=fake_data):
        result = get_transactions_from_json("anyfile.json")
    assert result == []


def test_get_transactions_from_json_empty_file(data_dir):
    empty_file = os.path.join(data_dir, "empty.json")
    with open(empty_file, "w", encoding="utf-8") as f:
        f.write("")
    assert get_transactions_from_json(empty_file) == []
