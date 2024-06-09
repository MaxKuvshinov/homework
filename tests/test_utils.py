import unittest
from unittest.mock import MagicMock, mock_open, patch

from src.utils import read_transactions


class TestGetTransactions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"transaction_id": 1, "amount": 100}]')
    @patch("os.path.exists", return_value=True)
    def test_read_transactions_valid_file(self, mock_exist: MagicMock, mock_open: MagicMock) -> None:
        transactions = read_transactions("test_file.json")
        self.assertEqual(transactions, [{"transaction_id": 1, "amount": 100}])

    @patch("builtins.open")
    def test_read_transactions_empty(self, mock_open: MagicMock) -> None:
        mock_open.return_value.__enter__.return_value.read.return_value = ""
        transactions = read_transactions("test_file.json")
        self.assertEqual(transactions, [])

    def test_read_transactions_not_found(self) -> None:
        transactions = read_transactions("nonexistent_file.json")
        self.assertEqual(transactions, [])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_transactions_file_not_found_with_patch(self, mock_open: MagicMock) -> None:
        transactions = read_transactions("test_file.json")
        self.assertEqual(transactions, [])
