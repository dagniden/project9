import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_card_number_generator() -> None:
    start, end = 1, 4
    cards = card_number_generator(start, end)

    with pytest.raises(StopIteration):
        assert next(cards) == "0000 0000 0000 0001"
        assert next(cards) == "0000 0000 0000 0002"
        assert next(cards) == "0000 0000 0000 0003"
        assert next(cards)  # Проверка завершения генератора


def test_transaction_descriptions(transactions: list) -> None:
    descriptions = transaction_descriptions(transactions)
    assert all(isinstance(x, str) for x in descriptions)
    assert all(isinstance(x, str) for x in descriptions)


def test_filter_by_currency(transactions: list[dict]) -> None:
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert all(transaction["operationAmount"]["currency"]["code"] == "USD" for transaction in usd_transactions)
    assert len(usd_transactions) == 3
