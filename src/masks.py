def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера карты"""

    temp_card_number = str(card_number)
    if len(temp_card_number) < 16 or len(temp_card_number) > 16:
        return "Неверный номер карты"
    else:
        return f"{temp_card_number[:4]} {temp_card_number[4:6]}** **** {temp_card_number[12:]}"


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера счета"""

    temp_account_number = str(account_number)
    if len(temp_account_number) < 20 or len(temp_account_number) > 20:
        return "Неверный номер счета"
    else:
        return f"**{temp_account_number[-4:]}"
