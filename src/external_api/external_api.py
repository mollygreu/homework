import os
from typing import Any
from typing import Dict

import requests


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли через внешний API.
    """
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    # Если уже в рублях — возвращаем как есть
    if currency == "RUB":
        return float(amount)

    api_key = os.getenv("API_KEY")
    url = os.getenv("API_URL")

    params = {
        "from": currency,
        "to": "RUB",
        "amount": amount
    }

    headers = {
        "apikey": api_key
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    return float(data["result"])
