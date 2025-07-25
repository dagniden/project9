"""Модуль с функциями для работы с транзакциями"""


def filter_by_state(transactions_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Возвращает новый список словарей, отфильтрованный по ключу state"""
    filtered_transactions = [x for x in transactions_list if x.get("state", None) == state]
    return filtered_transactions


def sort_by_date(transactions_list: list[dict], descending: bool = True) -> list[dict]:
    """Возвращает новый список словарей, отсортированный по ключу date"""
    sorted_transactions_list = sorted(transactions_list, key=lambda x: x.get("date", ""), reverse=descending)
    return sorted_transactions_list
