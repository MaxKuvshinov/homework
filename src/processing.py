from typing import List


def get_dicts_by_state(data: List[dict], state: str = "EXECUTED") -> List[dict]:
    """Функция, которая возвращает новый словарь"""
    filter_dict = []
    for item in data:
        if item.get("state") == state:
            filter_dict.append(item)
    return filter_dict


def sort_by_date(data: List[dict], reverse: bool = True) -> List[dict]:
    """Функция, которая сортирует список словарей по ключу 'date'."""
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
