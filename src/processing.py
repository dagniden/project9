"""Модуль с функциями для работы с транзакциями"""
import re
from src.utils import get_transactions_from_json
import json
from collections import Counter


def filter_by_state(transactions_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Возвращает новый список словарей, отфильтрованный по ключу state"""
    filtered_transactions = [x for x in transactions_list if x.get("state", None) == state]
    return filtered_transactions


def sort_by_date(transactions_list: list[dict], descending: bool = True) -> list[dict]:
    """Возвращает новый список словарей, отсортированный по ключу date"""
    sorted_transactions_list = sorted(transactions_list, key=lambda x: x.get("date", ""), reverse=descending)
    return sorted_transactions_list


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    pattern = rf'{search}'
    result = []

    for item in data:
        for key, value in item.items():
            res_keys = re.search(pattern, str(key), flags=re.IGNORECASE)
            res_values = re.search(pattern, str(value), flags=re.IGNORECASE)

            if res_keys or res_values:
                result.append(item)
                break  # переход к следующему item в data

    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    categories = [item.get('description') for item in data if item.get('description') in categories]
    counted = Counter(categories)
    return counted


def get_categories(data: list[dict]) -> list:
    categories = [item.get('description') for item in data ]
    return categories


if __name__ == "__main__":
    data_dict = get_transactions_from_json('operations.json')


    # all_categories = get_categories(data_dict)
    # print(all_categories)
    # counted = Counter(all_categories)
    # print(counted)

    counted = process_bank_operations(data_dict, ['Перевод организации', 'Открытие вклада'])
    print(counted)
