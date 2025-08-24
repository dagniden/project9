"""Модуль с функциями для работы с транзакциями"""
import re
from src.utils import get_transactions_from_json
import json


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
                break # переход к следующему item в data

    return result




if __name__ == "__main__":
    json_data = get_transactions_from_json('operations_short.json')
    print(json_data)

    filtered_list = process_bank_search(json_data, 'зеленый')
    print(filtered_list)
