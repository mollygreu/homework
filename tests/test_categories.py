from src.processing import process_bank_operations


def test_process_bank_operations():
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод другу"},
        {"description": "Оплата услуг"},
    ]
    categories = ["Перевод", "Оплата", "Вклад"]
    result = process_bank_operations(data, categories)

    assert result == {"Перевод": 2, "Оплата": 1, "Вклад": 1}
