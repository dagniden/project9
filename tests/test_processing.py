"""Модуль с автотестами для src.processing"""

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(transactions: list) -> None:
    # Проверяем работу параметра по умолчанию
    executed_transactions = filter_by_state(transactions)
    result_states_set = set([item.get("state", None) for item in executed_transactions])

    assert result_states_set == {"EXECUTED"}
    assert isinstance(executed_transactions, list)

    # Проверяем работу с параметром
    canceled_transactions = filter_by_state(transactions, "CANCELED")
    result_states_set = set([item.get("state", None) for item in canceled_transactions])
    assert result_states_set == {"CANCELED"}
    assert isinstance(canceled_transactions, list)

    # Проверка, что при с параметром, которого нет в словаре
    not_filtered_transactions = filter_by_state(transactions, "ABCD")
    assert not_filtered_transactions == []


def test_sort_by_date(transactions: list) -> None:
    # Параметры не отсортированного списка для проверки
    transactions_amount = len(transactions)
    transactions_dates_list = [item.get("date") for item in transactions]
    min_date = min(transactions_dates_list)
    max_date = max(transactions_dates_list)

    # Проверка сортировки по умолчанию (по убыванию)
    sorted_desc_transactions = sort_by_date(transactions)
    assert sorted_desc_transactions[0]["date"] == max_date
    assert sorted_desc_transactions[-1]["date"] == min_date
    assert len(sorted_desc_transactions) == transactions_amount

    # Проверка сортировки по возрастанию
    sorted_asc_transactions = sort_by_date(transactions, descending=False)
    assert sorted_asc_transactions[0]["date"] == min_date
    assert sorted_asc_transactions[-1]["date"] == max_date
    assert len(sorted_asc_transactions) == transactions_amount


@pytest.mark.parametrize(
    "invalid_transactions, expected",
    [
        ([{"date": "2019-0703"}], [{"date": "2019-0703"}]),
        ([{"date": ""}], [{"date": ""}]),
        ([{"dates": "2018-06-30T02:08:58.425572"}], [{"dates": "2018-06-30T02:08:58.425572"}]),
    ],
)
def test_sort_by_date_invalid(invalid_transactions: list, expected: list) -> None:
    assert sort_by_date(invalid_transactions) == expected
