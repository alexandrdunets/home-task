import json


def read_file_to_list(file_path: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    transactions = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if len(content) == 0:
            print("Данный файл пустой!")
            return transactions
        else:
            json_content = json.loads(content)

        if not isinstance(json_content, list):
            print("Данные по транзакциям должны быть оформлены в виде списка")
            return transactions

        if not json_content:
            print("Список транзакций пуст!")
            return transactions

        transactions = json_content

    except FileNotFoundError:
        print("Файл не найден, проверьте правильность указанного пути.")
        return transactions
    except json.JSONDecodeError as e:
        print("Ошибка декодирования JSON")
        return transactions

    print("Считывание файла: успешно")
    return transactions
