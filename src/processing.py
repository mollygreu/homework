"""Модуль для обработки списка банковских операций."""

from typing import Dict, Any


def filter_by_state(operations: list[Dict[str, Any]], state: str = "EXECUTED") -> list[Dict[str, Any]]:
    """
    Возвращает список операций с заданным состоянием.

    Args:
        operations (list[dict[str, Any]]): Список словарей с операциями.
        state (str): Статус операции (по умолчанию 'EXECUTED').

    Returns:
        list[dict[str, Any]]: Новый список с операциями, у которых state == указанному значению.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: list[Dict[str, Any]], reverse: bool = True) -> list[Dict[str, Any]]:
    """
    Сортирует список операций по дате.
    """
    operations_with_date = [op for op in operations if "date" in op]
    return sorted(operations_with_date, key=lambda x: x["date"], reverse=reverse)
