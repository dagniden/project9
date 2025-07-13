"""Модуль с автотестами для src.masks"""

import pytest

from src.masks import get_mask_account, get_mask_card_number
from tests.conftest import get_sample_accounts, get_sample_cards

RANDOM_TESTS_AMOUNT = 100


@pytest.mark.parametrize("card", get_sample_cards(RANDOM_TESTS_AMOUNT))
def test_get_mask_card_number(card: int) -> None:
    result = get_mask_card_number(card)
    assert len(result) == 19
    assert "**" in result and "****" in result
    assert str(card)[-4:] in result
    assert result.count(" ") == 3


@pytest.mark.parametrize("account", get_sample_accounts(RANDOM_TESTS_AMOUNT))
def test_get_mask_account(account: int) -> None:
    result = get_mask_account(account)
    assert len(result) == 6
    assert "**" in result
    assert str(account)[-4:] in result


@pytest.mark.parametrize("card, expected_error", [
                                                ("1", TypeError),
                                                (0, IndexError),
                                                ("", TypeError),
                                                ("a12345", TypeError)]
)
def test_get_mask_card_number_invalid(card, expected_error):
    with pytest.raises(expected_error):
        get_mask_card_number(card)


@pytest.mark.parametrize("account, expected_error", [(1, IndexError), ("1", TypeError), (0, IndexError), ("", TypeError)])
def test_get_mask_account_invalid(account, expected_error):
    with pytest.raises(expected_error):
        get_mask_account(account)
