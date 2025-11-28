from unittest.mock import patch

import pandas as pd

from src.readers.excel_reader import read_transactions_excel


@patch("pandas.read_excel")
def test_read_transactions_excel(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame([
        {"amount": 500, "currency": "RUB"}
    ])

    result = read_transactions_excel("fake.xlsx")

    assert len(result) == 1
    assert result[0]["currency"] == "RUB"
