import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"
    assert get_mask_card_number(12345678901234567890) == "Неверный номер карты"
    assert get_mask_card_number(123456789012) == "Неверный номер карты"


def test_get_mask_account():
    assert get_mask_account(12345678901234567890) == "**7890"
    assert get_mask_account(1234567890123456789012) == "Неверный номер счета"
    assert get_mask_account(123456789012) == "Неверный номер счета"