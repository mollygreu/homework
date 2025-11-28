from typing import Dict
from typing import List

import pandas as pd


def read_transactions_csv(file_path: str) -> List[Dict]:
    """
    Читает CSV-файл с транзакциями и возвращает список словарей.

    Args:
        file_path (str): Путь к CSV файлу.

    Returns:
        List[Dict]: Список транзакций в виде словарей.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return []
