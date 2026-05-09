import logging
from typing import Optional

logger = logging.getLogger(__name__)
logging.basicConfig(
    filemode="w"
)
file_handler = logging.FileHandler(
    filename="../h_task/logs/masks.log", encoding="utf-8"
)
file_formatter = logging.Formatter(
    "%(asctime)s %(name)s: %(levelname)s %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


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
        logger.error("Пользователь не ввел номер карты")
        raise ValueError("Номер карты отсутствует")

    if not isinstance(card_number, int | str):
        logger.error("Тип данных входного аргумента должен быть целым или строковым")
        raise TypeError("Тип данных входного аргумента должен быть целым или строковым")

    mask_card_number = ""
    number_str = str(card_number)

    if not number_str.isdigit():
        logger.error("Номер карты должен содержать только цифры")
        raise ValueError("Номер карты должен содержать только цифры")

    if len(number_str) != 16:
        logger.error("Номер карты должен содержать 16 цифр")
        raise ValueError("Номер карты должен содержать 16 цифр")

    mask_card_number = number_str[:4] + " " + number_str[4:6] + "** **** " + number_str[-4:]

    logger.info("Маска карты успешно сформирована")

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
        logger.error("Пользователь не ввел номер счета")
        raise ValueError("Номер счета отсутствует")

    if not isinstance(account_number, int | str):
        logger.error("Тип данных входного аргумента должен быть целым или строковым")
        raise TypeError("Тип данных входного аргумента должен быть целым или строковым")

    mask_account = ""
    account_str = str(account_number)

    if not account_str.isdigit():
        logger.error("Номер счета должен содержать только цифры")
        raise ValueError("Номер счета должен содержать только цифры")
    if len(account_str) != 20:
        logger.error("Номер счета должен содержать 20 цифр")
        raise ValueError("Номер счета должен содержать 20 цифр")

    mask_account = "**" + account_str[-4:]

    logger.info("Маска счета успешно сформирована")

    return mask_account
