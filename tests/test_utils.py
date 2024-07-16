import json
from unittest.mock import patch

from src.utils import get_data_transactions


@patch("builtins.open")
def test_get_data_transactions(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value

    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_data_transactions("test.json") == [{"test": "test"}]

    mock_file.read.return_value = json.dumps({})
    assert get_data_transactions("test.json") == []

    mock_file.read.return_value = json.dumps("testtest")
    assert get_data_transactions("test.json") == []

    mock_file.read.return_value = ""
    assert get_data_transactions("test.json") == []


@patch("pandas.read_csv")
def test_get_data_transactions_from_csv(mock_read_csv, transactions):
    mock_read_csv.return_value.to_dict.return_value = transactions
    assert get_data_transactions("data/transactions.csv") == transactions
    mock_read_csv.assert_called_once_with("data/transactions.csv", encoding="utf8")


@patch("pandas.read_excel")
def test_get_data_transactions_from_excel(mock_read_excel, transactions):
    mock_read_excel.return_value.to_dict.return_value = transactions
    assert get_data_transactions("data/transactions_excel.xlsx") == transactions
    mock_read_excel.assert_called_once_with("data/transactions_excel.xlsx")
