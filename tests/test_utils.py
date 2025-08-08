import os
from unittest.mock import MagicMock, patch

import pytest

from src.utils import get_transaction_amount_rub, get_transactions_from_json


def test_get_transactions_from_json(data_dir: str) -> None:
    file_path = os.path.join(data_dir, "operations.json")
    transactions_obj = get_transactions_from_json(file_path)
    assert type(transactions_obj) is list


def test_get_transactions_from_json_invalid_file(data_dir: str) -> None:
    file_path = os.path.join(data_dir, "abcdef.json")
    transactions_obj = get_transactions_from_json(file_path)
    assert transactions_obj == []


def test_get_transactions_from_json_invalid_data() -> None:
    fake_data = "abcd"
    with patch("json.load", return_value=fake_data):
        result = get_transactions_from_json("anyfile.json")
    assert result == []


def test_get_transactions_from_json_empty_file(data_dir: str) -> None:
    empty_file = os.path.join(data_dir, "empty.json")
    with open(empty_file, "w", encoding="utf-8") as f:
        f.write("")
    assert get_transactions_from_json(empty_file) == []


def test_amount_is_empty_raises() -> None:
    transaction = {"operationAmount": {"currency": {"code": "USD"}, "amount": ""}}
    with pytest.raises(ValueError, match="Invalid amount"):
        get_transaction_amount_rub(transaction)


def test_amount_is_not_float_raises() -> None:
    transaction = {"operationAmount": {"currency": {"code": "USD"}, "amount": "abc"}}
    with pytest.raises(ValueError, match="Invalid amount"):
        get_transaction_amount_rub(transaction)


def test_amount_rub_no_conversion() -> None:
    transaction = {"operationAmount": {"currency": {"code": "RUB"}, "amount": "150.50"}}
    result = get_transaction_amount_rub(transaction)
    assert result == 150.50


@patch("src.utils.get_amount_rub")
def test_amount_usd_conversion(mock_get_amount_rub: MagicMock) -> None:
    mock_get_amount_rub.return_value = 12345.67
    transaction = {"operationAmount": {"currency": {"code": "USD"}, "amount": "100"}}

    assert get_transaction_amount_rub(transaction) == 12345.67
    mock_get_amount_rub.assert_called_once_with(100.0, "USD")
