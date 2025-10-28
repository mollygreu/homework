import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_card_number_valid():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "input_val, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("0000000000000000", "0000 00** **** 0000"),
    ],
)
def test_get_mask_card_number_param(input_val, expected):
    assert get_mask_card_number(input_val) == expected


def test_get_mask_card_number_invalid_length():
    with pytest.raises(ValueError):
        get_mask_card_number("12345")  # слишком короткий


def test_get_mask_account_valid():
    assert get_mask_account("73654108430135874305") == "**4305"


@pytest.mark.parametrize(
    "input_val, expected",
    [
        ("12345", "**2345"),
        ("00001234", "**1234"),
    ],
)
def test_get_mask_account_param(input_val, expected):
    assert get_mask_account(input_val) == expected


def test_get_mask_account_invalid():
    with pytest.raises(ValueError):
        get_mask_account("12")  # меньше 4 цифр
