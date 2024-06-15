import masks


def mask_account_card(input_data: str) -> str:
    """Функция общей маскировки карты и счета"""

    if "Счет" in input_data:
        return input_data[:-20] + masks.get_mask_account(int(input_data[-20:]))
    else:
        return input_data[:-16] + masks.get_mask_card_number(int(input_data[-16:]))
