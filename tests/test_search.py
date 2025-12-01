import re
from src.processing import process_bank_search


def test_process_bank_search_found():
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод другу"},
    ]
    result = process_bank_search(data, "перевод")
    assert len(result) == 2
    assert all(re.search("перевод", op["description"], re.IGNORECASE) for op in result)


def test_process_bank_search_not_found():
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]
    result = process_bank_search(data, "кредит")
    assert result == []
