import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "number_card, expected",
    [("1234567890123456", "1234 56** **** 3456"), ("12345678901234567890", "Неверный номер карты")],
)
def test_get_mask_card_number(number_card, expected):
    assert get_mask_card_number(number_card) == expected


@pytest.mark.parametrize(
    "number_account, expected",
    [("12345678901234567890", "**7890"), ("1234567890123456", "Неверный номер счета")],
)
def test_get_mask_account(number_account, expected):
    assert get_mask_account(number_account) == expected
