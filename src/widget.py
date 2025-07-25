"""Модуль с функциями для работы с виджетом"""

from datetime import datetime

from src import masks


def mask_account_card(account_string: str) -> str:
    """Принимает номер счета или номер карты и возвращает замаскированный номер счета или номер карты"""

    if account_string == "":
        raise ValueError

    account_digits_list = [x for x in account_string if x.isdigit()]
    account_digits = int("".join(account_digits_list))
    account_prefix = "".join([x for x in account_string if x.isalpha() or x == " "]).strip()

    if "Счет" in account_prefix:
        masked_account = masks.get_mask_account(account_digits)
        return f"{account_prefix} {masked_account}"
    else:
        masked_card = masks.get_mask_card_number(account_digits)
        return f"{account_prefix} {masked_card}"


def get_date(date_time: str) -> str:
    """На вход принимает строку с датой в ISO формате и возвращает строку в формате ДД.ММ.ГГГГ"""
    try:
        dt = datetime.fromisoformat(date_time)
    except:
        raise ValueError
    return dt.strftime("%d.%m.%Y")
