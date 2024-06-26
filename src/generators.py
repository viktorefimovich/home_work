from typing import Dict, Generator, List


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

    for number in range(a, b+1):
        card_num_temp = f"{number:016}"
        generated_card_number = "".join(card_num_temp[i:i+4] for i in range(0, 16, 4))
        yield generated_card_number
