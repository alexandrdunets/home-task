import pytest


@pytest.fixture
def card_number_input_list_no_digit() -> list[str]:
    """Набор входных данных для негативного теста функции get_mask_card_number()"""
    return [
        "159683  7868705199",
        " 1596837868705199",
        "1596837868705199 ",
        "Card 1596837868705199",
        "15968378687O5199",
    ]


@pytest.fixture
def account_number_input_list_no_digit() -> list[str]:
    """Набор входных данных для негативного теста функции get_mask_account()"""
    return [
        "736541084 30135874305",
        " 73654108430135874305",
        "73654108430135874305 ",
        "Счет 73654108430135874305",
        "7365410843O135874305",
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