def get_dicts_by_state(data, state='EXECUTED'):
    """Функция, которая возвращает новый словарь"""
    filter_dict = []
    for item in data:
        if item.get("state") == state:
            filter_dict.append(item)
    return filter_dict
