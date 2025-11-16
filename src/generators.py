"""Модуль для работы с генераторами транзакций."""

from typing import Any
from typing import Dict
from typing import Iterator
from typing import List


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Возвращает итератор транзакций с указанной валютой.

    Args:
        transactions: список словарей транзакций
        currency_code: код валюты, например "USD"

    Returns:
        Итератор транзакций
    """
    for tx in transactions:
        if (
            "operationAmount" in tx
            and "currency" in tx["operationAmount"]
            and tx["operationAmount"]["currency"].get("code") == currency_code
        ):
            yield tx


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор, возвращающий описания транзакций.
    """
    for tx in transactions:
        if "description" in tx:
            yield tx["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номера банковской карты в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, stop + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[
            8:12] + " " + f"{number:016d}"[12:]
