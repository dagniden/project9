import os
from typing import Any
from src.utils import get_transactions_from_json
from src.data_reader import get_transactions_csv, get_transactions_xls
from src.processing import sort_by_date
from src.decorators import log


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

    # print(data)

    print("Отсортировать операции по дате? Да/Нет\n")
    user_sort_choice = get_user_input("Ваш выбор: ", ['да', 'нет'])
    if user_sort_choice == 'да':
        print("Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n")
        user_sort_asc_choice = get_user_input("Ваш выбор: ", ['по возрастанию', 'по убыванию'])

        if user_sort_asc_choice == 'по возрастанию':
            data = sort_by_date(data, descending=False)
        else:
            data = sort_by_date(data, descending=True)

    # print(data[:3])


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
