"""Модуль с функциями для работы с транзакциями"""

import re
from collections import Counter


def filter_by_state(transactions_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Возвращает новый список словарей, отфильтрованный по ключу state"""
    filtered_transactions = [x for x in transactions_list if x.get("state", None) == state]
    return filtered_transactions


def sort_by_date(transactions_list: list[dict], descending: bool = True) -> list[dict]:
    """Возвращает новый список словарей, отсортированный по ключу date"""
    sorted_transactions_list = sorted(transactions_list, key=lambda x: str(x.get("date", "")), reverse=descending)
    return sorted_transactions_list


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Фильтрует словарь по переданной строке поиска"""
    pattern = re.compile(search, flags=re.IGNORECASE)
    result = []

    for item in data:
        for key, value in item.items():
            if pattern.search(str(key)) or pattern.search(str(value)):
                result.append(item)
                break  # переход к следующему item в data

    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Возвращается словарь с подсчитанным количеством переданных категорий"""
    filtered_categories = [item.get("description") for item in data if item.get("description") in categories]
    counted_categories = Counter(filtered_categories)
    return counted_categories
