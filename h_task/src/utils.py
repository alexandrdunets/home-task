import json


def read_file_to_list(file_path: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    transactions = []

    try:
        with open(file_path, "r") as f:
            content = f.read()

            if not content:
                print("Данный файл пустой!")
                return transactions
            else:
                transactions = json.load(f)

        if not isinstance(transactions, list):
            print("Данные по транзакциям должны быть оформлены в виде списка")
            return transactions

    except FileNotFoundError:
        print("Файл не найден, проверьте правильность указанного пути.")
        return transactions

    return transactions


#print(read_file_to_list("../data/operations.json"))
