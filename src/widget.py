"""Модуль для работы с отображением информации о счетах и картах клиента."""

from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(info: str) -> str:
    """Маскирует номер карты или счёта, сохраняя тип (название).

    Пример:
        >>> mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'

        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'

    Args:
        info (str): Строка, содержащая тип и номер карты или счёта.

    Returns:
        str: Маскированная строка с типом и замаскированным номером.
    """
    # Разделяем входную строку на части
    parts = info.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    # Если строка начинается со слова "Счет" → применяем маску счёта
    if name.lower().startswith("счет"):
        masked = get_mask_account(int(number))
    else:
        # В противном случае применяем маску картыpoetry run flake8
        masked = get_mask_card_number(int(number))

    return f"{name} {masked}"


def get_date(date_str: str) -> str:
    """Преобразует дату из формата ISO 8601 в формат ДД.ММ.ГГГГ.

    Пример:
        >>> get_date("2024-03-11T02:26:18.671407")
        '11.03.2024'

    Args:
        date_str (str): Строка даты в формате 'YYYY-MM-DDTHH:MM:SS.microseconds'.

    Returns:
        str: Строка даты в формате 'DD.MM.YYYY'.
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
