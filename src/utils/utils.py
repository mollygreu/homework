import json
import logging
import os
from typing import Any
from typing import Dict
from typing import List

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# путь до файла logs/utils.log
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
LOG_PATH = os.path.join(ROOT_DIR, "logs", "utils.log")

# handler
file_handler = logging.FileHandler(LOG_PATH, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# formatter
formatter = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
)
file_handler.setFormatter(formatter)

# подключаем handler
logger.addHandler(file_handler)


def read_json(filepath: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список транзакций.
    Если файл пустой, не найден или содержит не список — возвращает [].
    """
    logger.debug(f"read_json вызвана с путем: {filepath}")

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                logger.info(f"Файл {filepath} успешно прочитан, найдено {len(data)} элементов")
                return data
            else:
                logger.warning(f"Файл {filepath} не содержит список, возвращаем пустой список")
                return []

    except FileNotFoundError:
        logger.error(f"Файл {filepath} не найден")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле {filepath}")
        return []
