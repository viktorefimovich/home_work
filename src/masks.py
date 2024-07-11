import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""

    logger.info("Проверяется номер карты")
    if len(card_number) != 16:
        logger.info("Неверный номер карты")
        return "Неверный номер карты"
    else:
        logger.info("Выводится замаскированный номер карты")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера счета"""

    logger.info("Проверяется номер счета")
    if len(account_number) != 20:
        logger.info("Неверный номер счета")
        return "Неверный номер счета"
    else:
        logger.info("Выводится замаскированный номер счета")
        return f"**{account_number[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("1234567890123450"))
    print(get_mask_account("12345678901234567890"))
