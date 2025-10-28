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

    Raises:
        ValueError: Если формат входных данных некорректен.
    """
    # Проверяем входные данные
    if not info or len(info.split()) < 2:
        raise ValueError("Неверный формат входных данных")

    parts = info.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if not number.isdigit():
        raise ValueError("Некорректный номер карты или счёта")

    # Если строка начинается со слова "Счет" → применяем маску счёта
    if name.lower().startswith("счет"):
        masked = get_mask_account(int(number))
    else:
        masked = get_mask_card_number(int(number))

    return f"{name} {masked}"


def get_date(date_str: str) -> str:
    """Преобразует дату из формата ISO 8601 в формат ДД.ММ.ГГГГ."""
    # Проверяем, что дата содержит символ 'T' (т.е. в формате с временем)
    if "T" not in date_str:
        raise ValueError("Неверный формат даты — отсутствует время")

    try:
        date_obj = datetime.fromisoformat(date_str)
    except Exception as exc:
        raise ValueError("Неверный формат даты") from exc
    return date_obj.strftime("%d.%m.%Y")
