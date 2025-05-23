import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')


def get_currency_usd_or_euro(transaction: dict) -> float | str:
    """Функция конвертации валюты если валюта не рубли"""
    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        rub = "RUB"
        amounts = float(transaction["operationAmount"]["amount"])
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={rub}&from={currency}&amount={amounts}"

        payload = {}
        headers = {
            "apikey": API_KEY
            }
        response = requests.request("GET", url, headers=headers, data=payload)

        if response.status_code != 200:
            raise Exception("Ошибка запроса к API")
        try:
            result = response.json()
            return result["result"]
        except requests.exceptions.JSONDecodeError:
            raise Exception("Ответ от API не в формате JSON")

    except Exception:
        raise Exception("Произошла ошибка с подключением")
    except KeyError:
        raise Exception("Отсутствует ключ в данных транзакции")
    except ValueError:
        raise Exception("Неверный формат суммы в транзакции")
    except requests.exceptions.RequestException:
        raise Exception("Ошибка при подключении к API")


def convert_to_rub(transaction: dict) -> float:
    """Функция возвращающая значение если валюта рубль"""
    if not isinstance(transaction, dict):
        return "Ошибка: transaction не является словарем."
    elif not transaction:
        return "Словарь пуст."
    elif transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        return get_currency_usd_or_euro(transaction)
