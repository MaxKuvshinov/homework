def filter_by_currency(transactions, currency_code):
    """Функция, которая принимает список словарей с банковскими операциями и возвращает итератор,
    который выдает по очереди операции, в которых указана заданная валюта."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction



def transaction_descriptions(transactions):
    """Генератор, который принимает список словарей и возвращает описание каждой опираций по очереди"""
    for transaction in transactions:
        yield transaction["description"]



def card_number_generator(start, stop):
    """Генератор номеров банковских карт, который генерирует номера карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра."""
    for number in range(start, stop + 1):
        card_number = f"{number:016}"
        formated_card_number = ' '.join(map(lambda i: card_number[i:i+4], range(0, 16, 4)))
        yield formated_card_number

for card_number in card_number_generator(1, 5):
    print(card_number)

