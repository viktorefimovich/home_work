import json
import logging
from pathlib import Path
from typing import Any

import pandas as pd

ROOTPATH = Path(__file__).resolve().parent.parent

logger = logging.getLogger("utils")
file_handler = logging.FileHandler(Path(ROOTPATH, "logs/utils.log"), "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_data_transactions(file_name: str) -> Any:
    """Функция, которая принимает на вход путь до файла и возвращает список словарей с данными о транзакциях"""

    try:
        if ".csv" in file_name:
            logger.info(f"Чтение CSV-файла: {file_name}")
            file_data = pd.read_csv(file_name, encoding="utf8")
            return file_data.to_dict(orient="records")
        elif ".json" in file_name:
            logger.info(f"Чтение JSON-файла: {file_name}")
            with open(file_name, encoding="utf-8") as f:
                data = json.load(f)
                logger.info(f"Файл {file_name} успешно прочитан.")

                if isinstance(data, list):
                    logger.info(f"Данные из {file_name} загружены как список.")
                    return data
                else:
                    logger.warning(f"Файл {file_name} не содержит список транзакций.")
                    return []
        elif ".xlsx" in file_name:
            logger.info(f"Чтение XLSX-файла: {file_name}")
            file_data = pd.read_excel(file_name)
            return file_data.to_dict(orient="records")
        else:
            logger.warning(f"Неподдерживаемый формат файла: {file_name}")
            return []
    except json.decoder.JSONDecodeError:
        logger.error(f"Ошибка декорирования JSON в файле {file_name}.")
        return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_name}.")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_name}: {e}")
        return []


if __name__ == "__main__":
    # Проверка JSON-файла
    transactions = get_data_transactions(str(Path(ROOTPATH, "data/operations.json")))
    if transactions:
        print("Список транзакций json-файла:")
        for transaction in transactions:
            print(transaction)
    else:
        print("Файл не найден, пустой или содержит некорректный формат.")

    # Проверка CSV-файла
    transactions_csv = get_data_transactions(str(Path(ROOTPATH, "data/transactions.csv")))
    if transactions_csv:
        print("Список транзакций из CSV-файла:")
        for transaction in transactions_csv:
            print(transaction)
    else:
        print("Ошибка при чтении CSV-файла.")

    # Проверка XLSX-файла
    transactions_excel = get_data_transactions(str(Path(ROOTPATH, "data/transactions_excel.xlsx")))
    if transactions_excel:
        print("\nСписок транзакций из XLSX-файла:")
        for transaction in transactions_excel:
            print(transaction)
    else:
        print("Ошибка при чтении XLSX-файла.")
