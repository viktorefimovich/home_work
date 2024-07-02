import json
from pathlib import Path
from typing import Any

from src.config import ROOT_PATH


def get_data_transactions(file_name: Path) -> Any:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о транзакциях"""

    try:
        with open(file_name, "r", encoding="utf-8") as f:
            try:
                data_transactions = json.load(f)
                return data_transactions
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []


if __name__ == "__main__":
    file_path = Path(ROOT_PATH, "../data/operations.json")
    result = get_data_transactions(file_path)
    print(result)
