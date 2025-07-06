from typing import List, Dict, Any


# В модуле processing напишите функцию filter_by_state, которая принимает список словарей и опционально значение для ключа
# state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
# state соответствует указанному значению.



# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

def filter_by_state(transactions_list: list[dict], state="EXECUTED") ->  list[dict]:
    filtered_transactions = [x for x in transactions_list if x.get("state", None) == state]
    return filtered_transactions

# В том же модуле напишите функцию sort_by_date, которая принимает список словарей и необязательный параметр, задающий порядок
# сортировки (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (
# date).


if __name__ == "__main__":
    # Пример входных данных
    data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    print("Входные данные")
    for i in data:
        print(i)

    print("\nВыходные данные")
    filtered_data = filter_by_state(data)
    for i in filtered_data:
        print(i)