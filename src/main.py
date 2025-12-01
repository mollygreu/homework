import json
import csv
from typing import Any

from src.processing import (
    filter_by_state,
    sort_by_date,
    process_bank_search,
    process_bank_operations,
)


AVAILABLE_STATUSES = {"EXECUTED", "CANCELED", "PENDING"}


def load_json(path: str) -> list[dict[str, Any]]:
    """Загружает JSON-файл."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def load_csv(path: str) -> list[dict[str, Any]]:
    """Загружает CSV-файл."""
    result = []
    try:
        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                result.append(row)
    except FileNotFoundError:
        return []
    return result


def load_xlsx(path: str) -> list[dict[str, Any]]:
    """Загружает XLSX-файл."""
    # Допустимое упрощение без pandas
    print("Поддержка XLSX не реализована.")
    return []


def main() -> None:
    """Основная логика программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор (1/2/3): ").strip()

    if choice == "1":
        data = load_json("data/operations.json")
    elif choice == "2":
        data = load_csv("data/operations.csv")
    elif choice == "3":
        data = load_xlsx("data/operations.xlsx")
    else:
        print("Некорректный выбор.")
        return

    if not data:
        print("Файл пустой или не найден.")
        return

    # выбор статуса
    while True:
        print("\nВведите статус для фильтрации (EXECUTED / CANCELED / PENDING)")
        status = input("Статус: ").strip().upper()

        if status in AVAILABLE_STATUSES:
            break

        print(f'Статус "{status}" недоступен.')

    filtered = filter_by_state(data, status)
    print(f'Операции отфильтрованы по статусу "{status}"')

    # сортировка
    if input("Отсортировать по дате? Да/Нет: ").lower() == "да":
        order = input("По возрастанию или по убыванию? ").lower()
        reverse = order != "по возрастанию"
        filtered = sort_by_date(filtered, reverse)

    # только рублевые
    if input("Выводить только рублевые? Да/Нет: ").lower() == "да":
        filtered = [op for op in filtered if op["operationAmount"]["currency"]["code"] == "RUB"]

    # поиск по слову
    if input("Отфильтровать по слову в описании? Да/Нет: ").lower() == "да":
        word = input("Введите слово: ")
        filtered = process_bank_search(filtered, word)

    if not filtered:
        print("Не найдено ни одной операции по условиям.")
        return

    print("\nРаспечатываю итоговый список транзакций...")
    print(f"Всего банковских операций: {len(filtered)}\n")

    for op in filtered:
        print(op)

    categories = ["Перевод", "Открытие", "Покупка", "Оплата"]
    stats = process_bank_operations(filtered, categories)

    print("\nСтатистика по категориям:")
    for cat, count in stats.items():
        print(f"{cat}: {count}")


if __name__ == "__main__":
    main()
