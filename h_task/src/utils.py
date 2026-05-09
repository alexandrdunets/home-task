import json

import logging


logger = logging.getLogger(__name__)
logging.basicConfig(
    filemode="w"
)
file_handler = logging.FileHandler(
    filename="../logs/utils.log", encoding="utf-8"
)
file_formatter = logging.Formatter(
    "%(asctime)s %(name)s: %(levelname)s %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_file_to_list(file_path: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    transactions = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if len(content) == 0:
            logger.error(f"Файл {file_path} пустой!")
            print("Данный файл пустой!")
            return transactions
        else:
            json_content = json.loads(content)

        if not isinstance(json_content, list):
            logger.error(f"Данные в файле {file_path} должны быть оформлены в виде списка!")
            print("Данные по транзакциям должны быть оформлены в виде списка")
            return transactions

        if not json_content:
            logger.error(f"Список транзакций в файле {file_path} пустой!")
            print("Список транзакций пуст!")
            return transactions

        transactions = json_content

    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден, проверьте правильность указанного пути.")
        print("Файл не найден, проверьте правильность указанного пути.")
        return transactions
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}")
        print("Ошибка декодирования JSON")
        return transactions

    logger.info(f"Считывание файла {file_path}: ok")
    print("Считывание файла: успешно")
    return transactions
