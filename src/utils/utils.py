import json
from typing import Any
from typing import Dict
from typing import List


def read_json(filepath: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список транзакций.
    Если файл пустой, не найден или содержит не список — возвращает [].
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data
            return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []
