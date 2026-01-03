from masks import get_mask_card_number, get_mask_account


def ask_account_card(account_card_str="") -> str:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты
    или счета, а возвращает строку с замаскированным номером."""

    account_card_mask = ""

    if account_card_str:
        if "счет" in account_card_str.lower():
            account_index = len(account_card_str) - len(account_card_str[-20:])
            account_card_mask = account_card_str[:account_index] + get_mask_account(account_card_str[account_index:])
        else:
            card_index = len(account_card_str) - len(account_card_str[-16:])
            account_card_mask = account_card_str[:card_index] + get_mask_card_number(account_card_str[card_index:])
    else:
        print("Значение карты или счета не должно быть пустым")

    return account_card_mask


def get_date(date_in="") -> str:
    """Функция get_date(date_in: str) принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")."""

    date_out = ""
    if date_in:
        day_dd = date_in[8: 10]
        month_mm = date_in[5: 7]
        year_yyyy = date_in[:4]
        if day_dd.isdigit() and month_mm.isdigit() and year_yyyy.isdigit():
            date_out = f"{day_dd}.{month_mm}.{year_yyyy}"
        else:
            print("Неправильный формат входных данных!")
    else:
        print("Аргумент не должен быть пустым!")

    return date_out
