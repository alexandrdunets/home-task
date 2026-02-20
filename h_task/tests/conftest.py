import pytest


@pytest.fixture
def card_number_input_list_no_digit() -> list[str | int]:
    """Набор входных данных для негативного теста функции get_mask_card_number()"""
    return [
        "159683  7868705199",
        " 1596837868705199",
        "1596837868705199 ",
        "Card 1596837868705199",
        "15968378687O5199",
        "-596837868705199",
        -596837868705199,
    ]


@pytest.fixture
def account_number_input_list_no_digit() -> list[str | int]:
    """Набор входных данных для негативного теста функции get_mask_account()"""
    return [
        "736541084 30135874305",
        " 73654108430135874305",
        "73654108430135874305 ",
        "Счет 73654108430135874305",
        "7365410843O135874305",
        "-3654108430135874305",
        -3654108430135874305,
    ]


@pytest.fixture
def ask_account_card_list_empty() -> list[str | None]:
    """Набор входных данных для негативного теста функции ask_account_card()
    на пустое значение"""
    return [None, ""]


@pytest.fixture
def account_card_list_invalid_input():
    """Набор входных данных для негативного теста функции ask_account_card()
    на несоответствие типа входных данных"""
    return [
        1,
        [
            1,
        ],
        (1,),
        {
            1,
        },
        {"key": "value"},
    ]


@pytest.fixture
def get_mask_card_account_list_invalid_input():
    """Набор входных данных для негативного теста функций get_mask_card_number()
    и get_mask_account() на несоответствие типа входных данных"""
    return [
        [
            1,
        ],
        (1,),
        {
            1,
        },
        {"key": "value"},
    ]


@pytest.fixture
def get_date_correct_format_list():
    """Набор входных данных с распознаваемым форматом"""
    return [
        "2024-03-11T02:26:18.671407",
        "  2024-03-11T02:26:18.671407   ",
        "2024-03-11T02:26   ",
        " 2024-03-11 ",
    ]


@pytest.fixture
def get_date_incorrect_format_list():
    """Набор входных данных с нераспознаваемым форматом"""
    return [
        "24-03-11T02:26:18.671407",
        "2024-O3-11T02:26:18.671407",
        "20 24-03-11T02:26   ",
        "T02:26:18.671407 2024-03-11 ",
        "2024-3-11T02:26:18.671407",
    ]


@pytest.fixture
def invalid_day_list():
    """Входные данные с некорректным днем месяца"""
    return ["2024-03-00T02:26:18.671407", "2024-03-32T02:26:18.671407"]


@pytest.fixture
def invalid_month_list():
    """Входные данные с некорректным месяцем"""
    return ["2024-00-11T02:26:18.671407", "2024-13-11T02:26:18.671407"]


@pytest.fixture
def filter_by_state_input():
    """Входные данные для проверки работы функции filter_by_state()"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def filter_by_state_executed_output():
    """Результат работы функции filter_by_state() с параметром state='EXECUTED' (по умолчанию)"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def filter_by_state_canceled_output():
    """Результат работы функции filter_by_state() с параметром state='CANCELED'"""
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def filter_by_state_empty_input():
    """Список словарей с пустым либо отсутствующим статусом 'state'"""
    return [
        {"id": 41428829, "state": "", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def another_status_input():
    """Список словарей со статусом 'state', отличающемся от указанного в аргументах функции filter_by_state()"""
    return [
        {"id": 594226727, "state": "ANY_1", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "ANY_2", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sort_by_date_input():
    """Список словарей в качестве входного аргумента функции sort_by_date()"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sort_by_date_decreasing_output():
    """Результат работы функции sort_by_date() с параметром is_descending=True (по умолчанию по убыванию)"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_by_date_increasing_output():
    """Результат работы функции sort_by_date() с параметром is_descending=False (по возрастанию)"""
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def sort_by_date_input_the_same_date():
    """Список словарей в качестве входного аргумента функции sort_by_date()
    с одинаковой датой"""
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def sort_by_date_decreasing_output_the_same_date():
    """Результат работы функции sort_by_date() с параметром is_descending=True (по умолчанию по убыванию)
    с одинаковой датой"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_by_date_increasing_output_the_same_date():
    """Результат работы функции sort_by_date() с параметром is_descending=False (по возрастанию)
    с одинаковой датой"""
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def invalid_type_input():
    """Список аргументов неподходящих типов для функций sort_by_date() и filter_by_state()"""
    return [
        1,
        1.1,
        "1",
        [1, 2],
        {"a": "b"},
        [{"a": "b"}, "a"],
        (1,),
        {
            1,
        },
    ]


@pytest.fixture
def invalid_format_date():
    """Список словарей с неподходящими форматами даты для функции sort_by_date()"""
    return [
        {"id": 939719570, "state": "EXECUTED", "date": 123},
        {"id": 939719570, "state": "EXECUTED", "date": [1, 2, 3]},
        {"id": 41428829, "state": "EXECUTED", "date": ""},
        {"id": 41428829, "state": "EXECUTED"},
        {"id": 939719570, "state": "EXECUTED", "date": "19-07-03T18:35:29.512364"},
    ]
