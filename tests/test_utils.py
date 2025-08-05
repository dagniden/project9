import json
from unittest.mock import Mock, patch

from src.utils import get_transactions_from_json
import os


def test_get_transactions_from_json():
    filename = "operations.json"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    file_path = os.path.join(data_dir, filename)

    transactions_obj = get_transactions_from_json(file_path)
    assert type(transactions_obj) == list


def test_get_transactions_from_json_invalid_file():
    filename = "abcdef.json"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    file_path = os.path.join(data_dir, filename)

    transactions_obj = get_transactions_from_json(file_path)
    assert transactions_obj == []



def test_get_transactions_from_json_invalid_data():
    fake_data = "abcd"
    with patch("json.load", return_value=fake_data):
        result = get_transactions_from_json("anyfile.json")
    assert result == []