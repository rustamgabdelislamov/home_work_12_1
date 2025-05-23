from src.utils import get_accepts_the_transaction

from unittest.mock import patch


@patch('json.load')
def test_get_accepts_the_transaction(mock_get):
    """Тест при правильном пути к Json"""
    mock_get.return_value = [{'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}}]
    path = 'data/operations.json'
    result = get_accepts_the_transaction(path)
    assert result == [{'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}}]


def test_test_get_accepts_the_transaction():
    """При неправильном пути к Json"""
    assert get_accepts_the_transaction("123.json") == []
