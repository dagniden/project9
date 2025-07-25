import pytest

from src.generators import card_number_generator, transaction_descriptions, filter_by_currency


def test_card_number_generator():
    start = 1
    end = 4
    cards = card_number_generator(start, end)
    with pytest.raises(StopIteration):
        assert next(cards) == "0000 0000 0000 0001"
        assert next(cards) == "0000 0000 0000 0002"
        assert next(cards) == "0000 0000 0000 0003"
        assert next(cards)


def test_transaction_descriptions():
    transaction_descriptions()


def test_filter_by_currency():
    filter_by_currency()
