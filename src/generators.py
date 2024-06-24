from typing import List, Dict


def filter_by_currency(data_transactions: List[Dict[str, dict]], currency: str):
    """Функция, которая выдает по очереди операции, в которых указана заданная валюта"""

    for transaction in data_transactions:
        if transaction["operationAmount"]["currency"].get("code") == currency:
            yield transaction["id"]
