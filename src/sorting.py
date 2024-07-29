import re
from pathlib import Path

from utils import get_data_transactions

ROOTPATH = Path(__file__).resolve().parent.parent


def get_transactions_sort_search(list_transactions: list[dict], search_string: str) -> list[dict]:
    sort_transactions = []
    for transaction in list_transactions:
        if "description" in transaction and re.search(search_string, transaction["description"], flags=re.IGNORECASE):
            sort_transactions.append(transaction)
    return sort_transactions


if __name__ == "__main__":
    search = input("Введите для поиска: ")
    transactions = get_data_transactions(str(Path(ROOTPATH, "data/operations.json")))

    print(get_transactions_sort_search(transactions, search))
