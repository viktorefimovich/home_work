import json
from unittest.mock import patch

from src.utils import get_data_transactions


def test_get_data_transactions():
    with patch("builtins.open") as mock_open:
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = json.dumps([{"test": "test"}])
        assert get_data_transactions("test.json") == [{"test": "test"}]
