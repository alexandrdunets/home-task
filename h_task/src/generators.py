from typing import Any, Dict, Generator, List, Optional


def filter_by_currency(
    list_dict: Optional[List[Dict]] = None, currency_code: Optional[str] = None
) -> Generator[dict, Any, None] | None:
    """Функция принимает на вход список словарей, представляющих транзакции и
    возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""

    if not list_dict:
        raise ValueError("Отсутствует словарь со входными данными")

    # Проверка типа данных входного аргумента
    if isinstance(list_dict, list):
        for item in list_dict:
            if not isinstance(item, dict):
                raise TypeError("Тип входного аргумента должен быть списком словарей")
    else:
        raise TypeError("Тип входного аргумента должен быть списком словарей")

    # Проверка на отсутствие значения currency_code во входном списке словарей
    if not any(x.get("operationAmount").get("currency").get("code") == currency_code for x in list_dict):
        raise ValueError("В словаре отсутствует информация по значению валюты")

    result = (
        transaction
        for transaction in list_dict
        if transaction.get("operationAmount").get("currency").get("code") == currency_code
    )

    return result


def transaction_descriptions(list_dict: Optional[List[Dict]] = None) -> Generator[Dict, None, None]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""

    if not list_dict:
        raise ValueError("Отсутствует словарь со входными данными")

    # Проверка типа данных входного аргумента
    if isinstance(list_dict, list):
        for item in list_dict:
            if not isinstance(item, dict):
                raise TypeError("Тип входного аргумента должен быть списком словарей")
    else:
        raise TypeError("Тип входного аргумента должен быть списком словарей")

    return (transaction.get("description") for transaction in list_dict)


def card_number_generator(
    begin_card_number: Optional[int] = None, end_card_number: Optional[int] = None
) -> Generator[str, None, None]:
    """Функция генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Параметры: begin_card_number - начальный номер, end_card_number - конечный номер генерации, они должны быть
     целыми положительными числами."""

    if not isinstance(begin_card_number, int) or not isinstance(end_card_number, int):
        raise TypeError("Тип входного аргумента должен быть целым")

    if begin_card_number > end_card_number:
        raise ValueError("Начальный номер генерации не должен превышать конечный")

    if 0 < begin_card_number <= 9999999999999999 and 0 < end_card_number <= 9999999999999999:

        for num in range(begin_card_number, end_card_number + 1):
            number = str(num).zfill(16)
            formatted_number = f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
            yield formatted_number
    else:
        raise ValueError("Входные параметры вне диапазона")
