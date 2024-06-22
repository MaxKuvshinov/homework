import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"


def conversion_in_rub(transaction: dict) -> Any:
    """Конвертация суммы транзакции в рубли"""
    try:
        amount = transaction.get("operationAmount", {}).get("amount")
        currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

        if currency == "RUB":
            return float(amount)

        if currency:
            response = requests.get(
                API_URL.format(to="RUB", from_=currency, amount=amount), headers={"apikey": API_KEY}
            )
            response.raise_for_status()
            data = response.json()
            return data.get("result", 0.0)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")

    return 0.0
