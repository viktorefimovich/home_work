from typing import List, Dict, Generator


def filter_by_currency(data_transactions: List[Dict], currency: str) -> Generator:
    """Функция, которая выдает по очереди операции, в которых указана заданная валюта"""

    for transaction in data_transactions:
        if transaction["operationAmount"]["currency"].get("code") == currency:
            yield transaction["id"]


# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions))


def transaction_descriptions(data_transactions: List[Dict]) -> Generator:
    """Функция, которая возвращает описание каждой операции по очереди."""

    for transaction in data_transactions:
        yield transaction["description"]


# descriptions = transaction_descriptions(transactions)
#
# for _ in range(5):
#     print(next(descriptions))


def card_number_generator(a: int, b: int) -> Generator:
    """Функция генератор номеров банковских карт"""

    while a <= b:
        card_num_temp = str(a + 10000000000000000)
        yield f"{card_num_temp[-16:-12]} {card_num_temp[-12:-8]} {card_num_temp[-8:-4]} {card_num_temp[-4:]}"
        a += 1


# for card_number in card_number_generator(100, 111):
#     print(card_number)
