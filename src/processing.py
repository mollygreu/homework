"""Модуль для обработки списка банковских операций."""

from typing import Any, List, Dict
import re
from collections import Counter


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


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Ищет операции по строке в поле 'description' с помощью регулярных выражений.

    Args:
        data (List[Dict]): список операций
        search (str): строка поиска

    Returns:
        List[Dict]: список операций, где description содержит строку поиска
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [item for item in data if pattern.search(item.get("description", ""))]


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Считает количество операций по заданным категориям на основе 'description'.

    Args:
        data (List[Dict]): список операций
        categories (List[str]): список категорий

    Returns:
        Dict[str, int]: словарь {категория: количество}
    """
    counter = Counter()

    for item in data:
        descr = item.get("description", "").lower()
        for cat in categories:
            if cat.lower() in descr:
                counter[cat] += 1

    return dict(counter)
