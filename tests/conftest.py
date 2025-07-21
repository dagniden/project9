import random

import pytest

CARD_NUMBER_LENGTH = 16
ACC_NUMBER_LENGTH = 20


def generate_card_number() -> int:
    """Возвращает строку с номером карты"""
    first_digit = str(random.randint(1, 9))
    new_card = [first_digit if x == 0 else str(random.randint(0, 9)) for x in range(CARD_NUMBER_LENGTH)]
    return int("".join(new_card))


def get_sample_cards(quantity: int) -> tuple:
    """Возвращает кортеж с заданным количеством номеров карт"""
    result = tuple([generate_card_number() for x in range(quantity)])
    return result


def generate_account_number() -> int:
    """Возвращает строку с номером аккаунта"""
    first_digit = str(random.randint(1, 9))
    new_account = [first_digit if x == 0 else str(random.randint(0, 9)) for x in range(ACC_NUMBER_LENGTH)]
    return int("".join(new_account))


def get_sample_accounts(quantity: int) -> tuple:
    """Возвращает кортеж с заданным количеством номеров аккаунтов"""
    result = tuple([generate_account_number() for x in range(quantity)])
    return result


@pytest.fixture
def transactions():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def account_cards():
    return [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]


if __name__ == "__main__":

    cards = get_sample_cards(10)
    print(type(cards))
    for i in cards:
        print(i)

    accounts = get_sample_accounts(10)
    for i in accounts:
        print(i)
