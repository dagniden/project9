"""Модуль с функциями для маскировки номера счета или карты"""

def get_mask_card_number(card_number: int) -> str:
    """Маскирует номер карты, показывая первые 6 и последние 4 цифры, остальное — звёздочки"""
    card_number_str = str(card_number)
    blocks = [card_number_str[i : i + 4] for i in range(0, 13, 4)]
    blocks[1] = blocks[1][0:2] + "**"
    blocks[2] = "****"
    return " ".join(blocks)


def get_mask_account(account_number: int) -> str:
    """Маскирует номер счета, показывая последние 4 цифры и 2 звёздочки перед ними"""
    return "**" + str(account_number)[-4:]


if __name__ == "__main__":
    # Запуск функций модуля с тестовыми данными
    masked_account = get_mask_account(73654108430135874305)
    masked_card_num = get_mask_card_number(7000792289606361)
    print(f"{masked_account=}, {masked_card_num=}")
