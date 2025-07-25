"""Модуль с функциями для маскировки номера счета или карты"""


def get_mask_card_number(card_number: int) -> str:
    """Маскирует номер карты, показывая первые 6 и последние 4 цифры, остальное — звёздочки"""
    if not isinstance(card_number, int):
        raise TypeError

    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        raise IndexError

    blocks = [card_number_str[i : i + 4] for i in range(0, 13, 4)]
    blocks[1] = blocks[1][0:2] + "**"
    blocks[2] = "****"
    return " ".join(blocks)


def get_mask_account(account_number: int) -> str:
    """Маскирует номер счета, показывая последние 4 цифры и 2 звёздочки перед ними"""
    if not isinstance(account_number, int):
        raise TypeError

    account_number_str = str(account_number)
    if len(account_number_str) != 20:
        raise IndexError

    return "**" + account_number_str[-4:]
