import random

import pytest

CARD_NUMBER_LENGTH = 16
ACC_NUMBER_LENGTH = 20


def generate_card_number() -> int:
    """Возвращает строку с номером карты"""
    new_card = [str(random.randint(0, 9)) for x in range(CARD_NUMBER_LENGTH)]
    return int("".join(new_card))


def get_sample_cards(quantity: int) -> tuple:
    """Возвращает кортеж с заданным количеством номеров карт"""
    result = tuple([generate_card_number() for x in range(quantity)])
    return result


def generate_account_number() -> int:
    """Возвращает строку с номером аккаунта"""
    new_account = [str(random.randint(0, 9)) for x in range(ACC_NUMBER_LENGTH)]
    return int("".join(new_account))


def get_sample_accounts(quantity: int) -> tuple:
    """Возвращает кортеж с заданным количеством номеров аккаунтов"""
    result = tuple([generate_account_number() for x in range(quantity)])
    return result


if __name__ == "__main__":

    cards = get_sample_cards(10)
    print(type(cards))
    for i in cards:
        print(i)

    accounts = get_sample_accounts(10)
    for i in accounts:
        print(i)
