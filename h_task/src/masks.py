from typing import Optional


def get_mask_card_number(card_number: Optional[int | str] = None) -> str:
    """Функция get_mask_card_number принимает на вход номер карты
    в виде числа и возвращает ее маску. Номер карты замаскирован
    и отображается в формате XXXX XX** **** XXXX,
    где X — это цифра номера. То есть видны первые 6 цифр и
    последние 4 цифры, остальные символы отображаются звездочками,
    номер разбит по блокам по 4 цифры, разделенным пробелами.
    Пример работы функции:
    7000792289606361     # входной аргумент
    7000 79** **** 6361  # выход функции"""

    if not card_number:
        raise ValueError("Номер карты отсутствует")

    mask_card_number = ""
    number_str = str(card_number)

    if not number_str.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")
    if len(number_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    mask_card_number = number_str[:4] + " " + number_str[4:6] + "** **** " + number_str[-4:]

    return mask_card_number


def get_mask_account(account_number: Optional[int | str] = None) -> str:
    """Функция get_mask_account принимает на вход номер счета в виде числа
    и возвращает его маску. Номер счета замаскирован и отображается
    в формате **XXXX, где X — это цифра номера. То есть видны
    только последние 4 цифры номера, а перед ними — две звездочки.
    Пример работы функции:
    73654108430135874305  # входной аргумент
    **4305  # выход функции"""

    if not account_number:
        raise ValueError("Номер счета отсутствует")

    mask_account = ""
    account_str = str(account_number)

    if not account_str.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")
    if len(account_str) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")

    mask_account = "**" + account_str[-4:]

    return mask_account
