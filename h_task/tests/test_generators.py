import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_usd_filter_by_currency(input_data_transactions, output_data_usd_transactions):
    """Тест для функции filter_by_currency() с аргументом currency_code = 'USD'"""
    usd_transactions = list(filter_by_currency(input_data_transactions, "USD"))
    assert usd_transactions == output_data_usd_transactions


def test_rub_filter_by_currency(input_data_transactions, output_data_rub_transactions):
    """Тест для функции filter_by_currency() с аргументом currency_code = 'RUB'"""
    usd_transactions = list(filter_by_currency(input_data_transactions, "RUB"))
    assert usd_transactions == output_data_rub_transactions


def test_filter_by_currency_empty_input():
    """Тест на отсутствие списка словарей входных данных"""
    with pytest.raises(ValueError) as exc_info:
        filter_by_currency()
    assert str(exc_info.value) == "Отсутствует словарь со входными данными"


def test_filter_by_currency_invalid_type_input(invalid_type_input):
    """Тест на неправильный тип входных данных функции filter_by_currency()"""
    for item in invalid_type_input:
        with pytest.raises(TypeError) as exc_info:
            filter_by_currency(item)
        assert str(exc_info.value) == "Тип входного аргумента должен быть списком словарей"


def test_filter_by_currency_invalid_operation(filter_by_currency_invalid_operation):
    """Тест на отсутствие информации по значению валюты в аргументе list_dict"""
    with pytest.raises(ValueError) as exc_info:
        filter_by_currency(filter_by_currency_invalid_operation, "USD")
    assert str(exc_info.value) == "В словаре отсутствует информация по значению валюты"


def test_filter_by_currency_invalid_operation_eu(input_data_transactions):
    """Тест на отсутствие информации по значению валюты в аргументе currency_code"""
    with pytest.raises(ValueError) as exc_info:
        filter_by_currency(input_data_transactions, "EU")
    assert str(exc_info.value) == "В словаре отсутствует информация по значению валюты"


def test_transaction_descriptions(input_data_transactions, transaction_descriptions_output):
    """Тест корректной работы функции transaction_descriptions() с корректными входными данными"""
    descriptions = transaction_descriptions(input_data_transactions)
    assert list(descriptions) == transaction_descriptions_output


def test_transaction_descriptions_empty_input():
    """Тест на отсутствие списка словарей входных данных"""
    with pytest.raises(ValueError) as exc_info:
        transaction_descriptions([])
    assert str(exc_info.value) == "Отсутствует словарь со входными данными"


def test_transaction_descriptions_invalid_type_input(invalid_type_input):
    """Тест на неправильный тип входных данных функции transaction_descriptions()"""
    with pytest.raises(TypeError) as exc_info:
        transaction_descriptions(invalid_type_input)
    assert str(exc_info.value) == "Тип входного аргумента должен быть списком словарей"


def test_transaction_empty_descriptions(transaction_empty_descriptions_input, transaction_empty_descriptions_output):
    """Тест корректной работы функции transaction_descriptions() с отсутствующими полями 'description'"""
    descriptions = transaction_descriptions(transaction_empty_descriptions_input)
    assert list(descriptions) == transaction_empty_descriptions_output


def test_card_number_generator(card_number_generator_output):
    """Тест корректной работы функции card_number_generator() с корректными входными данными"""
    card_number = card_number_generator(1, 5)
    assert list(card_number) == card_number_generator_output


@pytest.mark.parametrize(
    "x, y",
    [
        (0, 5),
        (-1, 3),
        (-3, -1),
        (1, 9999999999999999 + 1),
    ],
)
def test_card_number_generator_invalid_type_input(x, y):
    """Тест на нарушение диапазона входных данных функции card_number_generator()"""
    card_number = card_number_generator(x, y)
    with pytest.raises(ValueError) as exc_info:
        next(card_number)
    assert str(exc_info.value) == "Входные параметры вне диапазона"


def test_card_number_generator_incorrect_start_stop():
    """Тест на на превышение начального значения генерации над конечным для card_number_generator()"""
    card_number = card_number_generator(5, 1)
    with pytest.raises(ValueError) as exc_info:
        next(card_number)
    assert str(exc_info.value) == "Начальный номер генерации не должен превышать конечный"


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 1, "0000 0000 0000 0001"),
        (9999999999999999, 9999999999999999, "9999 9999 9999 9999"),
    ],
)
def test_card_number_generator_boundary_conditions(x, y, expected):
    """Тест на корректную работу функции card_number_generator() при крайних значениях диапазона"""
    card_number = card_number_generator(x, y)
    assert next(card_number) == expected
