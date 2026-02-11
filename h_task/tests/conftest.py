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
    return [1, [1,], (1,), {1,}, {"key": "value"},]


@pytest.fixture
def get_mask_card_account_list_invalid_input():
    """Набор входных данных для негативного теста функций get_mask_card_number()
    и get_mask_account() на несоответствие типа входных данных"""
    return [[1,], (1,), {1,}, {"key": "value"},]


@pytest.fixture
def get_date_correct_format_list():
    return [
        "2024-03-11T02:26:18.671407",
        "  2024-03-11T02:26:18.671407   ",
        "2024-03-11T02:26   ",
        " 2024-03-11 ",
    ]


@pytest.fixture
def get_date_incorrect_format_list():
    return [
        "24-03-11T02:26:18.671407",
        "2024-O3-11T02:26:18.671407",
        "20 24-03-11T02:26   ",
        "T02:26:18.671407 2024-03-11 ",
        "2024-3-11T02:26:18.671407"
    ]


@pytest.fixture
def invalid_day_list():
    return [
        "2024-03-00T02:26:18.671407",
        "2024-03-32T02:26:18.671407"
    ]


@pytest.fixture
def invalid_month_list():
    return [
        "2024-00-11T02:26:18.671407",
        "2024-13-11T02:26:18.671407"
    ]
