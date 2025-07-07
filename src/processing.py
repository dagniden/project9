"""Модуль с функциями для работы с транзакциями"""


def filter_by_state(transactions_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Возвращает новый список словарей, отфильтрованный по ключу state"""
    filtered_transactions = [x for x in transactions_list if x.get("state", None) == state]
    return filtered_transactions


def sort_by_date(transactions_list: list[dict], ascending: bool = False) -> list[dict]:
    """Возвращает новый список словарей, отсортированный по ключу date"""
    sorted_transactions_list = sorted(transactions_list, key=lambda x: x["date"], reverse=not ascending)
    return sorted_transactions_list


if __name__ == "__main__":
    # Запуск функций модуля с тестовыми данными
    test_data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print("Входные тестовые данные:")
    for item in test_data:
        print(item)

    filtered_data = filter_by_state(test_data)
    print("\nДанные после фильтрации:")
    for item in filtered_data:
        print(item)

    ascending = False
    sorted_data = sort_by_date(test_data, ascending)
    print(f"\nДанные после сортировки, {ascending=}: ")
    for item in sorted_data:
        print(item)
