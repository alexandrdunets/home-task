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