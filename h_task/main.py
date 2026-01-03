from src.widget import ask_account_card, get_date


def main():
    """Проверка работы функций"""

    print(ask_account_card("Maestro 1596837868705199"))
    print(ask_account_card("Счет 64686473678894779589"))
    print(ask_account_card("MasterCard 7158300734726758"))
    print(ask_account_card("Счет 35383033474447895560"))
    print(ask_account_card("Visa Classic 6831982476737658"))
    print(ask_account_card("Visa Platinum 8990922113665229"))
    print(ask_account_card("Visa Gold 5999414228426353"))
    print(ask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))


if __name__ == "__main__":
    main()
