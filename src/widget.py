"""Модуль с функциями для работы с виджетом"""

from datetime import datetime

from src import masks


def mask_account_card(account_string: str) -> str:
    """Принимает номер счета или номер карты и возвращает замаскированный номер счета или номер карты"""
    account_digits_list = [x for x in account_string if x.isdigit()]
    account_digits = int("".join(account_digits_list))
    account_prefix = "".join([x for x in account_string if x.isalpha() or x == " "])

    if "Счет" in account_prefix:
        masked_account = masks.get_mask_account(account_digits)
        return f"{account_prefix} {masked_account}"
    else:
        masked_card = masks.get_mask_card_number(account_digits)
        return f"{account_prefix} {masked_card}"


def get_date(date_time: str) -> str:
    """На вход принимает строку с датой в ISO формате и возвращает строку в формате ДД.ММ.ГГГГ"""
    dt = datetime.fromisoformat(date_time)
    return dt.strftime("%d.%m.%Y")


if __name__ == "__main__":
    # Запуск функций модуля с тестовыми данными
    test_account_cards = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]

    for item in test_account_cards:
        print(mask_account_card(item))
    pass

    test_date = "2024-03-11T02:26:18.671407"
    print(get_date(test_date))
