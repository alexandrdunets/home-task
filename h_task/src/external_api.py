import json
from typing import Any
import requests


def transaction_rub_amount(transaction: dict) -> float | None | Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли."""

    if not isinstance(transaction, dict):
        raise TypeError("Тип входного аргумента должен быть словарем")

    if not transaction:
        raise ValueError("Отсутствует словарь со входными данными")

    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if not currency_code:
        raise ValueError("В словаре отсутствует информация по значению валюты")

    amount = round(float(transaction.get("operationAmount", {}).get("amount", 0)), 2)

    if not amount:
        raise ValueError("В словаре отсутствует информация о сумме транзакции")

    date = transaction.get("date")

    if not date:
        raise ValueError("В словаре отсутствует информация о дате транзакции")

    date = date[:10]

    if currency_code == "RUB":
        return amount

    if currency_code == "EUR" or currency_code == "USD":
        return convert_to_rub(currency_code, amount, date)

    print("Значение валюты не является 'EUR' или 'USD'")
    return None


def convert_to_rub(currency_code: str, amount: float, date: str) -> float | None:
    """Функция выполняет обращение к внешнему API для получения текущего курса валют и конвертации
    суммы операции в рубли. Для конвертации валюты используется Exchange Rates Data API:
    https://apilayer.com/exchangerates_data-api."""

    url = "https://api.apilayer.com/exchangerates_data/convert"

    payload = {
        "date": date,
        "amount": amount,
        "from": currency_code,
        "to": "RUB"
    }

    headers = {
        "apikey": "JQ72bAiIKsqp12JGcL6BLsySVZcA28LH"
    }

    try:
        response = requests.get(url, params=payload, headers=headers)
        status_code = response.status_code
        print(f"status_code = {status_code}")
        response.raise_for_status()
        resp_dict = json.loads(response.text)
        res = round(float(resp_dict.get("result", 0)), 2)
        return res
    except requests.exceptions.ConnectionError:
        print("Ошибка подключения. Пожалуйста, проверьте ваше сетевое подключение.")
    except requests.exceptions.HTTPError:
        print("Ошибка HTTP. Пожалуйста, проверьте URL.")
    except requests.exceptions.RequestException:
        print("Произошла ошибка. Пожалуйста, повторите попытку позже.")




# print(convert_to_rub("USD", 1, "2000-08-26"))
# print(convert_to_rub("EUR", 1, "2000-08-26"))
print(transaction_rub_amount({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }))
