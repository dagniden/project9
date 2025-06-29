"""Модуль содержит функции для работы с новыми возможностями приложения"""

import masks


def mask_account_card(account_card: str) -> str:
    """Возвращает замаскированный номер счета или номер карты"""
    numbers_list = [x for x in account_card if x.isdigit()]
    numbers = int("".join(numbers_list))
    prefix = "".join([x for x in account_card if x.isalpha() or x == " "])

    if "Счет" in prefix:
        masked_account = masks.get_mask_account(numbers)
        return f"{prefix} {masked_account}"
    else:
        masked_card = masks.get_mask_card_number(numbers)
        return f"{prefix} {masked_card}"


def get_date(datetime: str) -> str:
    pass


if __name__ == "__main__":
    test_account_cards = ["Maestro 1596837868705199",
                          "Счет 64686473678894779589",
                          "MasterCard 7158300734726758",
                          "Счет 35383033474447895560",
                          "Visa Classic 6831982476737658",
                          "Visa Platinum 8990922113665229",
                          "Visa Gold 5999414228426353",
                          "Счет 73654108430135874305"]

    for item in test_account_cards:
        print(mask_account_card(item))
    pass
