import json
import os


def read_transactions(file_path: str) -> list[dict]:
    """Функция принимающая на вход путь до JSON-файла
     и возвращающая список словарей с финансовыми транзакциями """

    if not os.path.exists(file_path):  # Проверка существования файла по указанному пути
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Открытие файла
            data = json.load(file)
            if not isinstance(data, list):  # Проверка, что данные являются списком
                return []

            return data

    except json.JSONDecodeError:  # Случай ошибки декодирования JSON
        return []
