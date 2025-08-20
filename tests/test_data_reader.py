from src.data_reader import get_transactions_xls, get_transactions_csv
from unittest.mock import Mock, patch

import pandas as pd


def test_get_transactions_csv() -> None:
    sample_dict = {'PassengerId': [1, 2, 3, 4, 5],
                   'Survived': [0, 1, 1, 1, 0]}

    df = pd.DataFrame(sample_dict)

    with patch('pandas.read_csv', return_value=df):
        result = get_transactions_csv('test.file')

        expected = df.to_dict(orient='records')
        assert result == expected
