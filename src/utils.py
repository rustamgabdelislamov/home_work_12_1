import json


def get_accepts_the_transaction(path: str) -> list[dict]:
    """Функция принимает транзакцию в json и возвращает в виде списка словарей"""
    try:
        with open(path, 'r', encoding='utf-8') as transactions_json:
            transactions_api = json.load(transactions_json)
            if isinstance(transactions_api, list) and transactions_api != '':
                return transactions_api
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


path = '../data/operations.json'

transactions_list = (get_accepts_the_transaction(path))

if __name__ == "__main__":
    print(transactions_list[0])
