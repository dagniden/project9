def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маску номера банковской карты.

    Функция принимает полный номер карты и возвращает его маску
    в формате XXXX XX** **** XXXX: видны первые 6 цифр и последние 4 цифры,
    остальные символы заменены звёздочками. Номер разбивается на блоки
    по 4 цифры, разделённые пробелами.

    Пример вызова:
        get_mask_card_number(7000792289606361)
    Пример вывода:
        '7000 79** **** 6361'

    Аргументы:
        card_number (int): Полный номер банковской карты.

    Возвращает:
        str: Маска номера карты в формате XXXX XX** **** XXXX.
    """
    card_number_str = str(card_number)
    blocks = [card_number_str[i : i + 4] for i in range(0, 13, 4)]
    blocks[1] = blocks[1][0:2] + "**"
    blocks[2] = "****"
    return " ".join(blocks)


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маску номера счёта.

    Функция принимает полный номер счёта и возвращает его маску
    в формате **XXXX, где видны только последние четыре цифры,
    а перед ними стоят две звёздочки.

    Пример вызова:
         get_mask_account(73654108430135874305)
    Пример вывода:
        **4305

    Аргументы:
    - account_number (int): Полный номер счёта.

    Возвращает:
    - str: Маска номера счёта в формате **XXXX.
    """
    return "**" + str(account_number)[-4:]


if __name__ == "__main__":
    masked_account = get_mask_account(73654108430135874305)
    masked_card_num = get_mask_card_number(7000792289606361)
    print(f"{masked_account=}, {masked_card_num=}")
