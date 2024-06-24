def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""

    if len(card_number) != 16:
        return "Неверный номер карты"
    else:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера счета"""

    if len(account_number) != 20:
        return "Неверный номер счета"
    else:
        return f"**{account_number[-4:]}"
