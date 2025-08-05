from unittest.mock import Mock, patch

from src.external_api import convert_currency


def test_convert_currency_success():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"query": {"from": "USD", "to": "RUB", "amount": 8456.1}, "result": 676482}

    with patch("requests.get", return_value=mock_response):
        result = convert_currency(8463.45, "USD")
        assert result == 676482
