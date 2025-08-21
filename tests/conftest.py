import os
import random

import pandas as pd
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
def transactions() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def data_dir() -> str:
    """Возвращает путь к директории с данными"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    return data_dir


@pytest.fixture
def transactions_df():
    sample_dict = {
        "id": [1, 2, 3, 4],
        "state": ["EXECUTED", "PENDING", "EXECUTED", "PENDING"],
        "currency_code": ["EUR", "RUB", "SEK", "RUB"],
    }
    # sample_dict = {'PassengerId': [1, 2, 3, 4, 5],
    #                'Survived': [0, 1, 1, 1, 0]}

    # df = pd.DataFrame(sample_dict)
    return pd.DataFrame(sample_dict)
