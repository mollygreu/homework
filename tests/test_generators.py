import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


@pytest.fixture
def sample_transactions():
    return [
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "A"},
        {"operationAmount": {"currency": {"code": "RUB"}}, "description": "B"},
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "C"},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "D"},
    ]


def test_filter_by_currency_usd(sample_transactions):
    usd_iter = filter_by_currency(sample_transactions, "USD")
    result = list(usd_iter)
    assert len(result) == 2
    assert result[0]["description"] == "A"
    assert result[1]["description"] == "C"


def test_filter_by_currency_empty(sample_transactions):
    eur_iter = filter_by_currency(sample_transactions, "GBP")
    assert list(eur_iter) == []


def test_transaction_descriptions(sample_transactions):
    desc_iter = transaction_descriptions(sample_transactions)
    assert list(desc_iter) == ["A", "B", "C", "D"]


@pytest.mark.parametrize("start,stop,expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
])
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected
