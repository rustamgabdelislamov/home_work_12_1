from unittest.mock import patch

import pytest

from src.external_api import get_currency_usd_or_euro, convert_to_rub


@patch('requests.request')
def test_get_currency_usd_or_euro_usd_success(mock_request):
    """Тест если есть сеть и валюта USD"""
    mock_response = mock_request.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {'result': 100.0}

    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {"code": "USD"}
        }
    }
    result = get_currency_usd_or_euro(transaction)
    assert result == 100.0


@patch('requests.request')
def test_get_currency_usd_or_euro_usd_error(mock_request):
    """Тест если есть нет сети и валюта USD"""
    mock_response = mock_request.return_value
    mock_response.status_code = 500
    mock_response.json.return_value = {}
    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {"code": "USD"}
        }
    }
    with pytest.raises(Exception):
        get_currency_usd_or_euro(transaction)


def test_convert_to_rub_rub():
    """Тест если валюта RUB """
    transaction = {
        "operationAmount": {
            "amount": 10,
            "currency": {"code": "RUB"}
        }
    }
    result = convert_to_rub(transaction)
    assert result == 10


def test_convert_to_rub_empty():
    """Тест если пустой словарь """
    transaction = {}
    result = convert_to_rub(transaction)
    assert result == "Словарь пуст."


def test_convert_to_rub_not_dict():
    """Тест если не словарь """
    transaction = ''
    result = convert_to_rub(transaction)
    assert result == "Ошибка: transaction не является словарем."
