import os

from src.decorators import log
from src.external_api import conversion_in_rub
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.processing import get_dicts_by_state, sort_by_date
from src.utils import read_transactions
from src.widget import get_change_date, get_mask_account_card

print(get_mask_account_card("Visa Platinum 899092211366522"))

print(get_mask_account_card("Счет 73654108430135874305"))

print(get_change_date("2018-07-11T02:26:18.671407"))

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(get_dicts_by_state(data))

print(get_dicts_by_state(data, state="CANCELED"))

print(sort_by_date(data))


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")

for transaction in range(2):
    print(next(usd_transactions)["id"])

descriptions = transaction_descriptions(transactions)

for transaction in range(5):
    print(next(descriptions))


for card_number in card_number_generator(1, 5):
    print(card_number)


# @log(filename="mylog.txt")
# def my_function(x: int, y: int) -> int:
#     return x + y
#
#
# my_function(1, 2)
#
#
# @log(filename="mylog.txt")
# def my_function_error(x: int, y: int) -> float:
#     return x / y
#
#
# my_function_error(3, 0)

now_dir = os.path.dirname(os.path.abspath(__file__))
file_path_json = os.path.join(now_dir, "data", "transactions_excel.xlsx")
print(read_transactions(file_path_json))


transactions = read_transactions(file_path_json)


for transaction in transactions:
    rub_amount = conversion_in_rub(transaction)

    print(f"Сумма транзакции в RUB: {rub_amount}")
