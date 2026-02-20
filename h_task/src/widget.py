from typing import Optional

from src.masks import get_mask_account, get_mask_card_number


def ask_account_card(account_card_str: Optional[str] = None) -> str:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты
    или счета, а возвращает строку с замаскированным номером."""

    account_card_mask = ""

    if not account_card_str:
        raise ValueError("Отсутствуют название и номер карты (счета)")

    if not isinstance(account_card_str, str):
        raise TypeError("Тип входного аргумента должен быть строковым")

    account_card_list = []
    account_card_str = account_card_str.strip()
    account_card_list = account_card_str.split()

    if "счет" in account_card_str.lower():

        account_number = account_card_list.pop()
        account_card_mask = " ".join(account_card_list) + " " + get_mask_account(account_number)

    else:

        card_number = account_card_list.pop()
        account_card_mask = " ".join(account_card_list) + " " + get_mask_card_number(card_number)

    return account_card_mask


def get_date(date_in: Optional[str] = None) -> str:
    """Функция get_date(date_in: str) принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")."""

    date_out = ""

    if not date_in:
        raise ValueError("Отсутствует значение даты")

    if not isinstance(date_in, str):
        raise TypeError("Тип входного аргумента должен быть строковым")

    date_in = date_in.strip()

    day_dd = date_in[8:10]
    month_mm = date_in[5:7]
    year_yyyy = date_in[:4]

    if not day_dd.isdigit() or not month_mm.isdigit() or not year_yyyy.isdigit():
        raise ValueError("Нераспознанный формат входных данных!")

    if int(day_dd) not in range(1, 32):
        raise ValueError("В месяце должно быть от 1 до 31 дня")

    if int(month_mm) not in range(1, 13):
        raise ValueError("В году должно быть от 1 до 12 месяцев")

    date_out = f"{day_dd}.{month_mm}.{year_yyyy}"

    return date_out
