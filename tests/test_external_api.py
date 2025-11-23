from unittest.mock import MagicMock
from unittest.mock import patch

from src.external_api.external_api import convert_to_rub


@patch("requests.get")
def test_convert_usd(mock_get):
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"result": 9500.0}
    mock_get.return_value = mock_resp

    transaction = {
        "operationAmount": {
            "amount": 100,
            "currency": {"code": "USD"}
        }
    }

    assert convert_to_rub(transaction) == 9500.0
