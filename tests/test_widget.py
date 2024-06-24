import pytest

from src.widget import mask_account_card, get_data


@pytest.mark.parametrize(
    "input_data, expected",
    [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"), ("Счет 35383033474447895560", "Счет **5560")],
)
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize(
    "date_input, expected",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2018-07-11", "Неверный формат даты"),
        ("", "Неверный формат даты"),
    ],
)
def test_get_data(date_input, expected):
    assert get_data(date_input) == expected
