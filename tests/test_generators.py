from typing import Iterable

import pytest
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: Iterable[dict]) -> None:
    usd_filter_currency = filter_by_currency(transactions, "USD")
    rub_filter_currency = filter_by_currency(transactions, "RUB")
    next(usd_filter_currency)
    assert next(usd_filter_currency) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(rub_filter_currency) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


def test_transaction_descriptions(transactions: Iterable[dict]) -> None:
    descript_transaction = transaction_descriptions(transactions)
    assert next(descript_transaction) == "Перевод организации"
    assert next(descript_transaction) == "Перевод со счета на счет"
    assert next(descript_transaction) == "Перевод со счета на счет"
    assert next(descript_transaction) == "Перевод с карты на карту"
    assert next(descript_transaction) == "Перевод организации"


def test_card_number_generator() -> None:
    card_numbers = card_number_generator(1, 6)
    assert next(card_numbers) == "0000 0000 0000 0001"
    assert next(card_numbers) == "0000 0000 0000 0002"
    assert next(card_numbers) == "0000 0000 0000 0003"
    assert next(card_numbers) == "0000 0000 0000 0004"
    assert next(card_numbers) == "0000 0000 0000 0005"
    assert next(card_numbers) == "0000 0000 0000 0006"
