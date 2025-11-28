from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state_executed():
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]
    result = filter_by_state(data)
    assert result == [{"id": 1, "state": "EXECUTED"}]


def test_filter_by_state_canceled():
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]
    result = filter_by_state(data, "CANCELED")
    assert result == [{"id": 2, "state": "CANCELED"}]


def test_sort_by_date_descending():
    data = [
        {"id": 1, "date": "2020-01-01T00:00:00.000000"},
        {"id": 2, "date": "2021-01-01T00:00:00.000000"},
    ]
    result = sort_by_date(data)
    assert result[0]["id"] == 2


def test_sort_by_date_ascending():
    data = [
        {"id": 1, "date": "2020-01-01T00:00:00.000000"},
        {"id": 2, "date": "2021-01-01T00:00:00.000000"},
    ]
    result = sort_by_date(data, reverse=False)
    assert result[0]["id"] == 1
