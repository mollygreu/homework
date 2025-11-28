from unittest.mock import patch

import pandas as pd

from src.readers.csv_reader import read_transactions_csv


@patch("pandas.read_csv")
def test_read_transactions_csv(mock_read_csv):
    mock_read_csv.return_value = pd.DataFrame([
        {"amount": 100, "currency": "USD"},
        {"amount": 200, "currency": "EUR"},
    ])

    result = read_transactions_csv("fake.csv")

    assert len(result) == 2
    assert result[0]["amount"] == 100
