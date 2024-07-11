import json
import logging
from pathlib import Path
from typing import Any

from config import ROOT_PATH

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_data_transactions(file_name: Path) -> Any:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о транзакциях"""

    try:
        logger.info(f"Открытие JSON-файла {file_name}")
        with open(file_name, "r", encoding="utf-8") as f:
            try:
                logger.info("Получение списка транзакций")
                data_transactions = json.load(f)
                return data_transactions
            except json.JSONDecodeError:
                logger.error("Ошибка декодирования файла")
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        logger.error("Файл не найден")
        print("Файл не найден")
        return []


if __name__ == "__main__":
    file_path = Path(ROOT_PATH, "data/operations.json")
    transactions = get_data_transactions(file_path)
    logger.info("Вывод списка транзакций")
    print(transactions)
