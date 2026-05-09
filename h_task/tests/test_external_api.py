from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub, transaction_rub_amount


def test_transaction_rub_amount_from_rub(transaction_rub):
    """Тест на успешную обработку транзакции в рублях"""

    assert transaction_rub_amount(transaction_rub) == 31957.58


def test_transaction_rub_amount_wrong_type():
    """Тест на некорректный тип входных данных"""

    with pytest.raises(TypeError) as exc_info:
        transaction_rub_amount(["a", "b", "c"])
    assert str(exc_info.value) == "Тип входного аргумента должен быть словарем"


def test_convert_to_rub_empty_input():
    """Тест на пустой словарь по транзакции"""

    with pytest.raises(ValueError) as exc_info:
        transaction_rub_amount({})
    assert str(exc_info.value) == "Отсутствует словарь со входными данными"


def test_convert_to_rub_empty_currency(transaction_empty_currency):
    """Тест на отсутствие информации по типу валюты"""

    with pytest.raises(ValueError) as exc_info:
        transaction_rub_amount(transaction_empty_currency)
    assert str(exc_info.value) == "В словаре отсутствует информация по значению валюты"


def test_convert_to_rub_empty_amount(transaction_empty_amount):
    """Тест на отсутствие информации по сумме транзакции"""

    with pytest.raises(ValueError) as exc_info:
        transaction_rub_amount(transaction_empty_amount)
    assert str(exc_info.value) == "В словаре отсутствует информация о сумме транзакции"


def test_convert_to_rub_empty_date(transaction_empty_date):
    """Тест на отсутствие информации по дате транзакции"""

    with pytest.raises(ValueError) as exc_info:
        transaction_rub_amount(transaction_empty_date)
    assert str(exc_info.value) == "В словаре отсутствует информация о дате транзакции"


def test_convert_to_rub_not_eur_or_usd(transaction_not_eur_or_usd, capsys):
    """Тест на конвертацию валюты, отличной от EUR или USD"""

    result = transaction_rub_amount(transaction_not_eur_or_usd)
    captured = capsys.readouterr()
    assert captured.out == "Значение валюты не является 'EUR' или 'USD'\n"
    assert result is None


@patch("requests.get")
def test_convert_to_rub(mock_get, convert_to_rub_response):
    """Тест, имитирующий запрос на API"""

    mock_get.status_code = 200
    mock_get.return_value.json.return_value = convert_to_rub_response
    assert convert_to_rub("USD", 1, "2019-07-03") == convert_to_rub_response
