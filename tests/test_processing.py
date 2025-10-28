from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state_default(sample_operations):
    result = filter_by_state(sample_operations)
    assert all(item["state"] == "EXECUTED" for item in result)
    assert len(result) == 2  # из фикстуры два EXECUTED


def test_filter_by_state_param(sample_operations):
    result = filter_by_state(sample_operations, state="CANCELED")
    assert all(item["state"] == "CANCELED" for item in result)
    assert len(result) == 2


def test_filter_by_state_no_match(sample_operations):
    result = filter_by_state(sample_operations, state="UNKNOWN")
    assert result == []


def test_sort_by_date_descending(sample_operations):
    result = sort_by_date(sample_operations, reverse=True)
    # первый элемент — самый поздний по дате (2019-07-03)
    assert result[0]["date"] == "2019-07-03T18:35:29.512364"


def test_sort_by_date_ascending(sample_operations):
    result = sort_by_date(sample_operations, reverse=False)
    assert result[0]["date"] == "2018-06-30T02:08:58.425572"


def test_sort_by_date_equal_dates():
    data = [
        {"id": 1, "date": "2020-01-01T00:00:00.000000"},
        {"id": 2, "date": "2020-01-01T00:00:00.000000"},
    ]
    result = sort_by_date(data)
    assert len(result) == 2  # порядок между равными датами допустим
