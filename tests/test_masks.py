"""Модуль с автотестами для src.masks"""

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [
    (73654108430135874305, "**4305"),
    (99990000555566661234, "**1234")
])
def test_get_mask_account(card_number, expected):
    assert get_mask_account(card_number) == expected


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"
