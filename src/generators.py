from typing import List, Dict


def filter_by_currency(data_transactions: List[Dict[str, dict]], currency: str):
    """Функция, которая выдает по очереди операции, в которых указана заданная валюта"""

    for transaction in data_transactions:
        if transaction["operationAmount"]["currency"].get("code") == currency:
            yield transaction["id"]


# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions))


def transaction_descriptions(data_transactions: List[Dict[str, dict]]):
    """Функция, которая возвращает описание каждой операции по очереди."""
    for transaction in data_transactions:
        yield transaction["description"]


# descriptions = transaction_descriptions(transactions)
#
# for _ in range(5):
#     print(next(descriptions))
