import os
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src.data_reader import get_transactions_csv, get_transactions_xls


@patch("pandas.read_csv")
def test_get_transactions_csv_mock(mock_read_csv: MagicMock, transactions_df: pd.DataFrame) -> None:
    mock_read_csv.return_value = transactions_df

    result = get_transactions_csv("test.file")
    expected = transactions_df.to_dict(orient="records")

    assert result == expected
    mock_read_csv.assert_called_once_with("test.file", encoding="utf-8", sep=";")


def test_get_transactions_csv_invalid_file(data_dir: str) -> None:
    file_path = os.path.join(data_dir, "invalid.csv")
    with pytest.raises(FileNotFoundError):
        get_transactions_csv(file_path)


@patch("pandas.read_excel")
def test_get_transactions_xls_mock(mock_read_xls: MagicMock, transactions_df: pd.DataFrame) -> None:
    mock_read_xls.return_value = transactions_df

    result = get_transactions_xls("test.file")
    expected = transactions_df.to_dict(orient="records")

    assert result == expected
    mock_read_xls.assert_called_once_with("test.file")


def test_get_transactions_xls_invalid_file(data_dir: str) -> None:
    file_path = os.path.join(data_dir, "invalid.xlsx")
    with pytest.raises(FileNotFoundError):
        get_transactions_xls(file_path)
