import os
import json
from pathlib import Path

from typing import Any

from dotenv import load_dotenv
import requests

from src.utils import transactions

load_dotenv()

ROOTPATH = Path(__file__).resolve().parent.parent
env_path = ROOTPATH / ".env"
load_dotenv(env_path)

apy_key = os.getenv("API_KEY")


def get_sum_transaction(transaction: Any) -> Any:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    """

    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": apy_key}
    response = requests.request("GET", url, headers=headers)
    result = response.json()

    return result["result"]


print(get_sum_transaction(transactions[1]))
