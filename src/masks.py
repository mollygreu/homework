"""Модуль для маскировки банковских реквизитов."""


def get_mask_card_number(card_number: int) -> str:
    """Возвращает маску номера банковской карты в формате XXXX XX** **** XXXX.

    Args:
        card_number (int): Номер банковской карты (16 цифр).

    Returns:
        str: Маскированный номер карты.
    """
    digits = str(card_number)
    if len(digits) != 16 or not digits.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Возвращает маску банковского счёта в формате **XXXX (последние 4 цифры).

    Args:
        account_number (int): Номер банковского счёта.

    Returns:
        str: Маскированный номер счёта.
    """
    # Проверяем длину и содержимое номера карты
    digits = str(account_number)
    if not digits.isdigit() or len(digits) < 4:
        raise ValueError("Номер счёта должен содержать только цифры и быть не короче 4 символов")
    # Формируем замаскированный номер
    return f"**{digits[-4:]}"
