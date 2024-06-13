def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера карты"""
    temp_card_number = str(card_number)

    return f"{temp_card_number[:4]} {temp_card_number[4:6]}** **** {temp_card_number[12:]}"


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера счета"""
    temp_account_number = str(account_number)

    return f"**{temp_account_number[-4:]}"
