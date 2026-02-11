import pytest
from src.widget import ask_account_card, get_date


def test_ask_card():
    """Тест для проверки, что функция корректно распознает и применяет нужный тип
    маскировки для карты"""
    assert ask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_ask_account():
    """Тест для проверки, что функция корректно распознает и применяет нужный тип
        маскировки для счета"""
    assert ask_account_card("Счет 64686473678894779589") == "Счет **9589"


@pytest.mark.parametrize("x, expected", [
        ("  Maestro 1596837868705199   ", "Maestro 1596 83** **** 5199"),
        (" Счет 64686473678894779589 ", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ])
def test_ask_account_card(x, expected):
    """Параметризованные тесты с разными типами карт и счетов
    для проверки универсальности функции."""
    assert ask_account_card(x) == expected


def test_ask_account_card_empty(ask_account_card_list_empty):
    """Тест на отсутствие информации о номере карты (счета)"""
    for item in ask_account_card_list_empty:
        with pytest.raises(ValueError) as exc_info:
            ask_account_card(item)
        assert str(exc_info.value) == "Отсутствуют название и номер карты (счета)"


def test_ask_account_card_invalid_type_input(account_card_list_invalid_input):
    """Тест на несоответствие типа входных данных"""
    for item in account_card_list_invalid_input:
        with pytest.raises(TypeError) as exc_info:
            ask_account_card(item)
        assert str(exc_info.value) == "Тип входного аргумента должен быть строковым"


def test_get_date():
    """Тест на правильность преобразования даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_empty(ask_account_card_list_empty):
    """Тест на отсутствие информации о дате"""
    for item in ask_account_card_list_empty:
        with pytest.raises(ValueError) as exc_info:
            get_date(item)
        assert str(exc_info.value) == "Отсутствует значение даты"


def test_get_date_invalid_type_input(account_card_list_invalid_input):
    """Тест на несоответствие типа входных данных"""
    for item in account_card_list_invalid_input:
        with pytest.raises(TypeError) as exc_info:
            get_date(item)
        assert str(exc_info.value) == "Тип входного аргумента должен быть строковым"


def test_get_date_acceptable_format(get_date_correct_format_list):
    """Положительный тест функции на различных входных форматах даты, включая
    нестандартные строки с датами."""
    for item in get_date_correct_format_list:
        assert get_date(item) == "11.03.2024"

def test_get_date_unacceptable_format(get_date_incorrect_format_list):
    """Негативный тест функции на различных входных форматах даты, включая
    нестандартные строки с датами."""
    for item in get_date_incorrect_format_list:
        with pytest.raises(ValueError) as exc_info:
            get_date(item)
        assert str(exc_info.value) == "Нераспознанный формат входных данных!"


def test_get_date_invalid_day(invalid_day_list):
    """Тест на граничные условия по количеству дней в месяце"""
    for item in invalid_day_list:
        with pytest.raises(ValueError) as exc_info:
            get_date(item)
        assert str(exc_info.value) == "В месяце должно быть от 1 до 31 дня"


def test_get_date_invalid_month(invalid_month_list):
    """Тест на граничные условия по количеству месяцев в году"""
    for item in invalid_month_list:
        with pytest.raises(ValueError) as exc_info:
            get_date(item)
        assert str(exc_info.value) == "В году должно быть от 1 до 12 месяцев"




