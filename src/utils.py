import json
import logging
import os
import re
from collections import Counter

import pandas as pd

log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")
os.makedirs(log_dir, exist_ok=True)
logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
log_filename = os.path.join(log_dir, "utils.log")
file_handler = logging.FileHandler(log_filename, mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions(file_path: str) -> list[dict]:
    """Функция принимающая на вход путь до JSON-файла
    и возвращающая список словарей с финансовыми транзакциями"""
    logger.info(f"Получение данных из файла {file_path}")

    try:
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == ".json":
            logger.info(f"Открытие JSON файла {file_path}")
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, list):
                    logger.info(f"Успешно прочитано {len(data)} транзакций из JSON файла")
                    return data
                else:
                    logger.warning(f"Данные из JSON файла не являются списком: {type(data)}")
                    return []

        elif file_extension == ".csv":
            logger.info(f"Открытие CSV файла {file_path}")
            df = pd.read_csv(file_path, sep=";")
            csv_transactions = []
            for index, row in df.iterrows():
                transaction = {
                    "id": row["id"],
                    "state": row["state"],
                    "date": row["date"],
                    "operationAmount": {
                        "amount": row["amount"],
                        "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                    },
                    "description": row["description"],
                    "from": row["from"],
                    "to": row["to"],
                }
                csv_transactions.append(transaction)
            logger.info(f"Успешно прочитано {len(csv_transactions)} транзакций из CSV файла")
            return csv_transactions

        elif file_extension == ".xlsx":
            logger.info(f"Открытие Excel файла {file_path}")
            df = pd.read_excel(file_path)
            excel_transactions = []
            for index, row in df.iterrows():
                transaction = {
                    "id": row["id"],
                    "state": row["state"],
                    "date": row["date"],
                    "operationAmount": {
                        "amount": row["amount"],
                        "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                    },
                    "description": row["description"],
                    "from": row["from"],
                    "to": row["to"],
                }
                excel_transactions.append(transaction)
            logger.info(f"Успешно прочитано {len(excel_transactions)} транзакций из Excel файла")
            return excel_transactions

        else:
            logger.warning(f"Формат файла не поддерживается: {file_extension}")
            return []

    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []

    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        return []


def search_description(transactions: list[dict], search_string: str) -> list[dict]:
    result = []
    pattern = re.compile(search_string, re.IGNORECASE)

    for item in transactions:
        description = item.get("description", "")
        if isinstance(description, str) and pattern.search(description):
            result.append(item)

    return result


def categorize_transactions(transactions: list[dict], categories: list[str]) -> dict:

    categories_count = Counter()

    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                categories_count[category] += 1

    return dict(categories_count)


