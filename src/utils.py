import json
import os

from utils_logger_config import logger


def read_transactions(file_path: str) -> list[dict]:
    """Функция принимающая на вход путь до JSON-файла
    и возвращающая список словарей с финансовыми транзакциями"""
    logger.info(f"Получение данных из файла {file_path}")

    if os.path.exists(file_path):  # Проверка существования файла по указанному пути
        try:
            logger.info(f"Открытие файла {file_path}")
            with open(file_path, "r", encoding="utf-8") as file:  # Открытие файла
                data = json.load(file)
                if isinstance(data, list):  # Проверка, что данные являются списком
                    logger.info(f'"Успешно прочитано {len(data)} транзакций')
                    return data
                else:
                    logger.warning(f"Данные не являются списком: {(type(data))}")
                    return []

        except json.JSONDecodeError as e:  # Случай ошибки декодирования JSON
            logger.error(f"Ошибка декодирования {e}")
            return []
        except Exception as e:  # Случай других ошибок
            logger.error(f"Ошибка при чтении файла: {e}")
            return []
    else:
        logger.error(f"Файл не найден {file_path}")
        return []
