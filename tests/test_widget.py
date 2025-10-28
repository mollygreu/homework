import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_param(input_str, expected):
    assert mask_account_card(input_str) == expected


def test_mask_account_card_invalid():
    with pytest.raises(ValueError):
        mask_account_card("Visa 123")  # номер слишком короткий или неверный формат


def test_get_date_valid():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize("input_val", ["2024-03-11", "11.03.2024", "", "not-a-date"])
def test_get_date_invalid(input_val):
    with pytest.raises(ValueError):
        # ожидаем ValueError при неверном формате
        get_date(input_val)
