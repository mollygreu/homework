"""Модуль для обработки списка банковских операций."""

from typing import Any


def filter_by_state(operations: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Возвращает список операций с заданным состоянием.

    Args:
        operations (list[dict[str, Any]]): Список словарей с операциями.
        state (str): Статус операции (по умолчанию 'EXECUTED').

    Returns:
        list[dict[str, Any]]: Новый список с операциями, у которых state == указанному значению.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """
    Сортирует список операций по дате.

    Args:
        operations (list[dict[str, Any]]): Список словарей с операциями.
        reverse (bool): Порядок сортировки (по умолчанию True — по убыванию).

    Returns:
        list[dict[str, Any]]: Новый отсортированный список.
    """
    return sorted(operations, key=lambda x: x.get("date", ""), reverse=reverse)
