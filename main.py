import json
import os
from typing import Any
from src.utils import get_transactions_from_json
from src.data_reader import get_transactions_csv, get_transactions_xls
from src.processing import sort_by_date, filter_by_state, process_bank_search
from src.decorators import log
from src.generators import filter_by_currency
from src.widget import get_date, mask_account_card


@log("main.log")
def main() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
          "Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из JSON-файла\n"
          "2. Получить информацию о транзакциях из CSV-файла\n"
          "3. Получить информацию о транзакциях из XLSX-файла\n")

    user_file_choice = get_user_input("Ваш выбор: ", [1, 2, 3])
    data = []
    if user_file_choice == 1:
        data = get_transactions_from_json(os.path.join(data_dir, "operations.json"))
    elif user_file_choice == 2:
        data = get_transactions_csv(os.path.join(data_dir, "transactions.csv"))
    elif user_file_choice == 3:
        data = get_transactions_xls(os.path.join(data_dir, "transactions_excel.xlsx"))

    print("Введите статус, по которому необходимо выполнить фильтрацию.\n"
          "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")
    user_filter_state_choice = get_user_input("Ваш выбор: ", ['executed', 'canceled', 'pending'])
    data = filter_by_state(data, user_filter_state_choice.upper())
    print(f'Операции отфильтрованы по статусу "{user_filter_state_choice.upper()}"')

    print("Отсортировать операции по дате? Да/Нет\n")
    user_sort_choice = get_user_input("Ваш выбор: ", ['да', 'нет'])
    if user_sort_choice == 'да':
        print("Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n")
        user_sort_asc_choice = get_user_input("Ваш выбор: ", ['по возрастанию', 'по убыванию'])
        if user_sort_asc_choice == 'по возрастанию':
            data = sort_by_date(data, descending=False)
        else:
            data = sort_by_date(data, descending=True)

    print("Выводить только рублевые транзакции? Да/Нет\n")
    user_filter_rub_choice = get_user_input("Ваш выбор: ", ['да', 'нет'])
    if user_filter_rub_choice == 'да':
        data = list(filter_by_currency(data, "RUB"))

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_filter_description_choice = get_user_input("Ваш выбор: ", ['да', 'нет'])
    if user_filter_description_choice == 'да':
        user_search = input("Введите строку для поиска: ")
        data = process_bank_search(data, user_search)

    data_len = len(data)
    if data_len == 0:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("\nРаспечатываю итоговый список транзакций...\n"
              f"Всего банковских операций в выборке: {data_len}\n")
        for result in data:
            try:
                tr_date = get_date(result['date'])
                tr_desc = result['description']
                tr_from = mask_account_card(result['from'])
                tr_to = mask_account_card(result['to'])
                if user_file_choice == 1:
                    tr_currency = result.get('operationAmount', {}).get('currency', {}).get('name')
                elif user_file_choice == 2 or user_file_choice == 3:
                    tr_currency = result.get('currency', None)

                if user_file_choice == 1:
                    tr_amount = result.get('operationAmount', {}).get('amount', None)
                elif user_file_choice == 2 or user_file_choice == 3:
                    tr_amount = result.get('amount', None)
            except Exception:
                continue

            print(f"{tr_date} {tr_desc}\n"
                  f"{tr_from} -> {tr_to}\n"
                  f"Сумма: {tr_amount} {tr_currency}\n\n")


def get_user_input(message: str, correct_choices: list) -> Any:
    while True:
        user_input = input(message)
        try:
            # Преобразуем ответ пользователя к типу правильного ответа
            user_choice = type(correct_choices[0])(user_input)

            if isinstance(user_choice, str):
                # Для корректного сравнения строк преобразуем к нижнему регистру
                user_choice = user_choice.lower()

            if user_choice in correct_choices:
                return user_choice
            else:
                print("Введено некорректное значение")
        except ValueError:
            print("Введено некорректное значение")


if __name__ == "__main__":
    main()
