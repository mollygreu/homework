"""Модуль для маскировки банковских реквизитов."""
import logging
import os

# логирование
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_PATH = os.path.join(ROOT_DIR, "logs", "masks.log")

file_handler = logging.FileHandler(LOG_PATH, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Возвращает маску номера банковской карты в формате XXXX XX** **** XXXX."""
    logger.debug(f"get_mask_card_number вызвана с аргументом: {card_number}")

    digits = str(card_number)
    if len(digits) != 16 or not digits.isdigit():
        logger.error("Ошибка: номер карты некорректный")
        raise ValueError("Номер карты должен состоять из 16 цифр")

    result = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
    logger.info(f"Успешная маскировка карты: {result}")

    return result


def get_mask_account(account_number: int) -> str:
    """Возвращает маску банковского счёта в формате **XXXX (последние 4 цифры)."""
    logger.debug(f"get_mask_account вызвана с аргументом: {account_number}")

    # Проверяем длину и содержимое номера карты
    digits = str(account_number)
    if not digits.isdigit() or len(digits) < 4:
        logger.error("Ошибка: номер счёта некорректный")
        raise ValueError("Номер счёта должен содержать только цифры и быть не короче 4 символов")

    # Формируем замаскированный номер
    result = f"**{digits[-4:]}"
    logger.info(f"Успешная маскировка счёта: {result}")

    return result
