import json


def read_file_to_list(file_path: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    transactions = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            transactions = json.load(f)

        if not  transactions:
            print("Данный файл пустой!")
            return transactions

        if not isinstance(transactions, list):
            print("Данные по транзакциям должны быть оформлены в виде списка")
            return transactions

    except FileNotFoundError:
        print("Файл не найден, проверьте правильность указанного пути.")
        return transactions

    return transactions

def qwe(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = json.load(f)

    return content


print(read_file_to_list("../data/operations.json"))
