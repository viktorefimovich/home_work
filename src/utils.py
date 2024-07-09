import json
from pathlib import Path
from typing import Any

from src.config import ROOT_PATH


def get_data_transactions(file_path: Any) -> Any:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о транзакциях"""

    try:
        with open(file_path, encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []


path_file = Path(ROOT_PATH, "../data/operations.json")
transactions = get_data_transactions(path_file)
print(transactions)
