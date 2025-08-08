from unittest.mock import Mock, patch

import pytest

from src.external_api import convert_currency


def test_convert_currency_success() -> None:
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"query": {"from": "USD", "to": "RUB", "amount": 1000}, "result": 5000}

    with patch("requests.get", return_value=mock_response):
        result = convert_currency(1000, "USD")
        assert result == 5000


def test_convert_currency_missing_api_key(monkeypatch) -> None:
    monkeypatch.delenv("API_KEY", raising=False)
    with pytest.raises(ValueError, match="API key not found"):
        convert_currency(100, "USD")


@pytest.mark.parametrize("status", [401, 403, 500])
def test_convert_currency_failed_status(status: str) -> None:
    mock_response = Mock()
    mock_response.status_code = status

    with patch("requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Failed to get conversion from external API"):
            convert_currency(100, "USD")


def test_convert_currency_no_result_in_response() -> None:
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"query": {"from": "USD", "to": "RUB", "amount": 100}, "result": None}

    with patch("requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="No data from conversion"):
            convert_currency(100, "USD")
