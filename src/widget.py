import masks
from datetime import datetime


def mask_account_card(input_data: str) -> str:
    """Функция общей маскировки карты и счета"""

    if "Счет" in input_data:
        return input_data[:-20] + masks.get_mask_account(int(input_data[-20:]))
    else:
        return input_data[:-16] + masks.get_mask_card_number(int(input_data[-16:]))


def get_data(date: str) -> str:
    """Функция преобразования даты"""

    date_it = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_it.strftime("%d.%m.%Y")


# if __name__ == "__main__":
#     print(get_data("2018-07-11T02:26:18.671407"))
