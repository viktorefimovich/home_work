import re
from collections import Counter
from pathlib import Path

from src.utils import get_data_transactions

ROOTPATH = Path(__file__).resolve().parent.parent


def get_transactions_sort_search(list_transactions: list[dict], search_string: str) -> list[dict]:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список
    словарей, у которых в описании есть данная строка
    """

    sort_transactions = []
    for transaction in list_transactions:
        if "description" in transaction and re.search(search_string, transaction["description"], flags=re.IGNORECASE):
            sort_transactions.append(transaction)
    return sort_transactions


if __name__ == "__main__":
    search = input("Введите для поиска: ")
    transactions = get_data_transactions(str(Path(ROOTPATH, "data/operations.json")))

    print(get_transactions_sort_search(transactions, search))


def get_list_category_description(list_transactions: list[dict], list_category: list) -> dict:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в
    каждой категории
    """

    list_category_description = []
    for transaction in list_transactions:
        if "description" in transaction and transaction["description"] in list_category:
            list_category_description.append(transaction["description"])
    sort_transaction = dict(Counter(list_category_description))
    return sort_transaction


if __name__ == "__main__":
    category = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод с карты на счет",
        "Перевод со счета на счет",
        "Открытие вклада",
    ]
    transactions = get_data_transactions(str(Path(ROOTPATH, "data/operations.json")))

    print(get_list_category_description(transactions, category))
