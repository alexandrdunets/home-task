import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    """Тест правильности маскирования номера карты"""
    assert get_mask_card_number(1596837868705199) == "1596 83** **** 5199"


def test_get_mask_card_number_less_than_16():
    """Тест на длину номера карты менее 16 цифр"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(159683786870519)
    assert str(exc_info.value) == "Номер карты должен содержать 16 цифр"


def test_get_mask_card_number_more_than_16():
    """Тест на длину номера карты более 16 цифр"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(15968378687051999)
    assert str(exc_info.value) == "Номер карты должен содержать 16 цифр"


def test_get_mask_card_number_no_digit(card_number_input_list_no_digit):
    """Тест на содержание в номере карты не цифровых символов"""
    for number in card_number_input_list_no_digit:
        with pytest.raises(ValueError) as exc_info:
            get_mask_card_number(number)
        assert str(exc_info.value) == "Номер карты должен содержать только цифры"


def test_get_mask_card_number_is_absent():
    """Тест на отсутствие номера карты"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number()
    assert str(exc_info.value) == "Номер карты отсутствует"


def test_get_mask_account():
    """Тест правильности маскирования номера счета"""
    assert get_mask_account(73654108430135874305) == "**4305"


def test_get_mask_account_less_than_20():
    """Тест на длину номера счета менее 20 цифр"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(7365410843013587430)
    assert str(exc_info.value) == "Номер счета должен содержать 20 цифр"


def test_get_mask_account_more_than_20():
    """Тест на длину номера счета более 20 цифр"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(7365410843013587430511)
    assert str(exc_info.value) == "Номер счета должен содержать 20 цифр"


def test_get_mask_account_no_digit(account_number_input_list_no_digit):
    """Тест на содержание в номере счета не цифровых символов"""
    for number in account_number_input_list_no_digit:
        with pytest.raises(ValueError) as exc_info:
            get_mask_account(number)
        assert str(exc_info.value) == "Номер счета должен содержать только цифры"


def test_get_mask_account_is_absent():
    """Тест на отсутствие номера счета"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account()
    assert str(exc_info.value) == "Номер счета отсутствует"
