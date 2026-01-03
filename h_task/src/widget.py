from masks import get_mask_card_number, get_mask_account


def ask_account_card(account_card_str: str) -> str | None:
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
