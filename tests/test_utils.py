# -*- coding: utf-8 -*-
import unittest
from unittest.mock import MagicMock, mock_open, patch

import pandas as pd
from src.utils import read_transactions


class TestReadTransactions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"transaction_id": 1, "amount": 100}]')
    @patch("os.path.exists", return_value=True)
    def test_read_transactions_valid_json(self, mock_exist: MagicMock, mock_open: MagicMock) -> None:
        transactions = read_transactions("test_file.json")
        self.assertEqual(transactions, [{"transaction_id": 1, "amount": 100}])

    @patch("builtins.open")
    def test_read_transactions_empty(self, mock_open: MagicMock) -> None:
        mock_open.return_value.__enter__.return_value.read.return_value = ""
        transactions = read_transactions("test_file.json")
        self.assertEqual(transactions, [])

    @patch("os.path.exists", return_value=False)
    def test_read_transactions_file_not_found(self, mock_exist: MagicMock) -> None:
        transactions = read_transactions("nonexistent_file.json")
        self.assertEqual(transactions, [])

    @patch("pandas.read_csv")
    def test_read_transactions_csv_file(self, mock_read_csv: MagicMock) -> None:
        mock_read_csv.return_value = pd.DataFrame(
            [
                {
                    "id": 650703,
                    "state": "EXECUTED",
                    "date": "2023-09-05T11:30:32Z",
                    "amount": 16210,
                    "currency_name": "Sol",
                    "currency_code": "PEN",
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                    "description": "Перевод организации",
                },
                {
                    "id": 3598919,
                    "state": "EXECUTED",
                    "date": "2020-12-06T23:00:58Z",
                    "amount": 29740,
                    "currency_name": "Peso",
                    "currency_code": "COP",
                    "from": "Discover 3172601889670065",
                    "to": "Discover 0720428384694643",
                    "description": "Перевод с карты на карту",
                },
            ]
        )
        transactions = read_transactions("test_file.csv")
        expected_transactions = [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "operationAmount": {"amount": 16210, "currency": {"name": "Sol", "code": "PEN"}},
                "description": "Перевод организации",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
            },
            {
                "id": 3598919,
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "operationAmount": {"amount": 29740, "currency": {"name": "Peso", "code": "COP"}},
                "description": "Перевод с карты на карту",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
            },
        ]
        self.assertEqual(transactions, expected_transactions)

    @patch("pandas.read_excel")
    def test_read_transactions_excel_file(self, mock_read_excel: MagicMock) -> None:
        mock_read_excel.return_value = pd.DataFrame(
            [
                {
                    "id": 650703,
                    "state": "EXECUTED",
                    "date": "2023-09-05T11:30:32Z",
                    "amount": 16210,
                    "currency_name": "Sol",
                    "currency_code": "PEN",
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                    "description": "Перевод организации",
                },
                {
                    "id": 3598919,
                    "state": "EXECUTED",
                    "date": "2020-12-06T23:00:58Z",
                    "amount": 29740,
                    "currency_name": "Peso",
                    "currency_code": "COP",
                    "from": "Discover 3172601889670065",
                    "to": "Discover 0720428384694643",
                    "description": "Перевод с карты на карту",
                },
            ]
        )
        transactions = read_transactions("test_file.xlsx")
        expected_transactions = [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "operationAmount": {"amount": 16210, "currency": {"name": "Sol", "code": "PEN"}},
                "description": "Перевод организации",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
            },
            {
                "id": 3598919,
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "operationAmount": {"amount": 29740, "currency": {"name": "Peso", "code": "COP"}},
                "description": "Перевод с карты на карту",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
            },
        ]
        self.assertEqual(transactions, expected_transactions)

    def test_read_transactions_unsupported_format(self) -> None:
        transactions = read_transactions("test_file.txt")
        self.assertEqual(transactions, [])

    @patch("builtins.open", new_callable=mock_open, read_data='{"transaction_id": 1, "amount": 100}')
    def test_read_transactions_malformed_json(self, mock_open: MagicMock) -> None:
        transactions = read_transactions("test_file.json")
        self.assertEqual(transactions, [])

    @patch("pandas.read_csv", side_effect=Exception("CSV read error"))
    def test_read_transactions_csv_read_error(self, mock_read_csv: MagicMock) -> None:
        transactions = read_transactions("test_file.csv")
        self.assertEqual(transactions, [])

    @patch("pandas.read_excel", side_effect=Exception("Excel read error"))
    def test_read_transactions_excel_read_error(self, mock_read_excel: MagicMock) -> None:
        transactions = read_transactions("test_file.xlsx")
        self.assertEqual(transactions, [])
