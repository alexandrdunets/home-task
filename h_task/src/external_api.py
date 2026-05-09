import os
from typing import Any

import requests
from dotenv import load_dotenv


def transaction_rub_amount(transaction: dict) -> float | None | Any:
    """Функция принимает на вход транзакцию в виде словаря и возвращает сумму транзакции (amount) в рублях,
    тип данных — float.
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
        result = convert_to_rub(currency_code, amount, date)
        if result:
            result = round(float(result.get("result")), 2)
            return result
        else:
            return None

    print("Значение валюты не является 'EUR' или 'USD'")
    return None


def convert_to_rub(currency_code: str, amount: float, date: str) -> dict | None:
    """Функция выполняет обращение к внешнему API для получения текущего курса валют и конвертации
    суммы операции в рубли. Для конвертации валюты используется Exchange Rates Data API:
    https://apilayer.com/exchangerates_data-api.
        В качестве входных аргументов используются currency_code (тип валюты), amount (сумма) и
    date (дата транзакции). Функция возвращает словарь с результатом конвертации валюты."""

    global result
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"date": date, "amount": amount, "from": currency_code, "to": "RUB"}

    # Загрузка переменных из .env-файла
    load_dotenv()
    # Получение значения переменной API_KEY из .env-файла
    api_key = os.getenv("API_KEY")

    headers = {"apikey": api_key}

    try:
        result = {}
        response = requests.get(url, params=payload, headers=headers)
        status_code = response.status_code
        print(f"status_code = {status_code}")

        if status_code == 200:
            # Вызываем метод json у объекта response, который возвращает ответ от API в виде словаря.
            result = response.json()

        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("Ошибка подключения. Пожалуйста, проверьте ваше сетевое подключение.")
    except requests.exceptions.HTTPError:
        print("Ошибка HTTP. Пожалуйста, проверьте URL.")
    except requests.exceptions.RequestException:
        print("Произошла ошибка. Пожалуйста, повторите попытку позже.")

    return result
