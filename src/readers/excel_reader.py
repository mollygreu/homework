from typing import Dict
from typing import List

import pandas as pd


def read_transactions_excel(file_path: str) -> List[Dict]:
    """
    Читает Excel-файл с транзакциями и возвращает список словарей.

    Args:
        file_path (str): Путь к Excel файлу.

    Returns:
        List[Dict]: Список транзакций в виде словарей.
    """
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except (FileNotFoundError, ValueError):
        return []
