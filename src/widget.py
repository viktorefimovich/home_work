from datetime import datetime
from typing import Any

from src import masks


def mask_account_card(input_data: str) -> Any:
    """Функция общей маскировки карты и счета"""

    if "Счет" in input_data:
        return input_data[:-20] + masks.get_mask_account(input_data[-20:])
    else:
        return input_data[:-16] + masks.get_mask_card_number(input_data[-16:])


def get_data(date: str) -> str:
    """Функция преобразования даты"""

    if len(date) != 26:
        return "Неверный формат даты"
    else:
        date_it = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_it.strftime("%d.%m.%Y")
