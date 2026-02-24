import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(filter_by_state_input, filter_by_state_executed_output):
    """Тестирование фильтрации списка словарей по статусу state="EXECUTED" (по умолчанию)."""
    assert filter_by_state(filter_by_state_input) == filter_by_state_executed_output


def test_filter_by_state_canceled(filter_by_state_input, filter_by_state_canceled_output):
    """Тестирование фильтрации списка словарей по статусу state="CANCELED"."""
    assert filter_by_state(filter_by_state_input, state="CANCELED") == filter_by_state_canceled_output


def test_filter_by_state_empty(filter_by_state_empty_input):
    """Тест на отсутствие ключа 'state' или значения по нему"""
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(filter_by_state_empty_input)
    assert str(exc_info.value) == "В словаре отсутствует информация по статусу state"


def test_filter_by_state_empty_input():
    """Тест на отсутствие списка словарей входных данных"""
    with pytest.raises(ValueError) as exc_info:
        filter_by_state()
    assert str(exc_info.value) == "Отсутствует словарь со входными данными"


def test_filter_by_another_status_input(another_status_input):
    """Тест на отсутствие словарей с указанным статусом 'state'"""
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(another_status_input)
    assert str(exc_info.value) == "Отсутствуют словари с указанным статусом 'state'"


def test_sort_by_date_decreasing(sort_by_date_input, sort_by_date_decreasing_output):
    """Тест работы функции sort_by_date() с параметром is_descending=True (по умолчанию по убыванию)"""
    assert sort_by_date(sort_by_date_input) == sort_by_date_decreasing_output


def test_sort_by_date_increasing(sort_by_date_input, sort_by_date_increasing_output):
    """Тест работы функции sort_by_date() с параметром is_descending=False (по возрастанию)"""
    assert sort_by_date(sort_by_date_input, is_descending=False) == sort_by_date_increasing_output


def test_sort_by_date_decreasing_the_same_date(
    sort_by_date_input_the_same_date, sort_by_date_decreasing_output_the_same_date
):
    """Тест работы функции sort_by_date() с параметром is_descending=True (по умолчанию по убыванию)
    с одинаковой датой"""
    assert sort_by_date(sort_by_date_input_the_same_date) == sort_by_date_decreasing_output_the_same_date


def test_sort_by_date_increasing_the_same_date(
    sort_by_date_input_the_same_date, sort_by_date_increasing_output_the_same_date
):
    """Тест работы функции sort_by_date() с параметром is_descending=False (по возрастанию)
    с одинаковой датой"""
    assert (
        sort_by_date(sort_by_date_input_the_same_date, is_descending=False)
        == sort_by_date_increasing_output_the_same_date
    )


def test_sort_by_date_empty_input():
    """Тест на отсутствие списка словарей входных данных функции sort_by_date()"""
    with pytest.raises(ValueError) as exc_info:
        sort_by_date()
    assert str(exc_info.value) == "Отсутствует список словарей для сортировки"


def test_sort_by_date_invalid_type_input(invalid_type_input):
    """Тест на неправильный тип входных данных функции sort_by_date()"""
    for item in invalid_type_input:
        with pytest.raises(TypeError) as exc_info:
            sort_by_date(item)
        assert str(exc_info.value) == "Тип входного аргумента должен быть списком словарей"


def test_filter_by_state_invalid_type_input(invalid_type_input):
    """Тест на неправильный тип входных данных функции filter_by_state()"""
    for item in invalid_type_input:
        with pytest.raises(TypeError) as exc_info:
            filter_by_state(item)
        assert str(exc_info.value) == "Тип входного аргумента должен быть списком словарей"


def test_invalid_format_date(invalid_format_date):
    """Тест с неподходящими форматами даты для функции sort_by_date()"""
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(invalid_format_date)
    assert str(exc_info.value) == "Неверный формат даты"
