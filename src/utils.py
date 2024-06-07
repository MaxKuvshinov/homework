import json
import os
import pprint


def read_transactions(file_path):
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

    except json.JSONDecodeError:  # Случай ошибка декодирования JSON
        return []


if __name__ == "__main__":
    now_dir = os.path.dirname(os.path.abspath(__file__))

    file_path_json = os.path.join(now_dir, '../data', 'operations.json')
    pprint.pprint(read_transactions(file_path_json))


















