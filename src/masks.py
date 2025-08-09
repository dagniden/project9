"""Модуль с функциями для маскировки номера счета или карты"""

import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(current_dir, "..", "logs")
os.makedirs(log_dir, exist_ok=True)  # создаём папку если её нет

log_file = os.path.join(log_dir, "masks.log")

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(log_file, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Маскирует номер карты, показывая первые 6 и последние 4 цифры, остальное — звёздочки"""
    if not isinstance(card_number, int):
        msg = "Card number is not integer"
        logger.error(msg)
        raise TypeError(msg)

    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        msg = "Card number length is not 16 chars"
        logger.error(msg)
        raise IndexError(msg)

    blocks = [card_number_str[i: i + 4] for i in range(0, 13, 4)]
    blocks[1] = blocks[1][0:2] + "**"
    blocks[2] = "****"

    result = " ".join(blocks)
    logger.info(f"Successfully masked card number: {result} for card number: {card_number}")
    return result


def get_mask_account(account_number: int) -> str:
    """Маскирует номер счета, показывая последние 4 цифры и 2 звёздочки перед ними"""
    if not isinstance(account_number, int):
        msg = "Account number is not integer"
        logger.error(msg)
        raise TypeError(msg)

    account_number_str = str(account_number)
    if len(account_number_str) != 20:
        msg = "Account number length is not 20 chars"
        logger.error(msg)
        raise IndexError(msg)

    result = "**" + account_number_str[-4:]
    logger.info(f"Successfully masked account number: {result} for account number: {account_number}")
    return result
