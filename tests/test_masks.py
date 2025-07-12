"""Модуль с автотестами для src.masks"""

import pytest

from src.masks import get_mask_account, get_mask_card_number
from tests.conftest import get_sample_accounts, get_sample_cards

TESTS_NUMBER = 100


@pytest.mark.parametrize("card", get_sample_cards(TESTS_NUMBER))
def test_get_mask_card_number(card: int) -> None:
    result = get_mask_card_number(card)
    assert len(result) == 19
    assert "**" in result
    assert str(card)[-4:] in result


@pytest.mark.parametrize("account", get_sample_accounts(TESTS_NUMBER))
def test_get_mask_account(account: int) -> None:
    result = get_mask_account(account)
    assert len(result) == 6
    assert "**" in result
    assert str(account)[-4:] in result
