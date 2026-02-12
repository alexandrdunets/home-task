import datetime
from typing import Optional


def filter_by_state(list_dict: Optional[list[dict]] = None, state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'),
    а возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению."""

    list_res_dict = []

    if not list_dict:
        raise ValueError("Отсутствует словарь со входными данными")

    # Проверка типа данных входного аргумента
    if isinstance(list_dict, list):
        for item in list_dict:
            if not isinstance(item, dict):
                raise TypeError("Тип входного аргумента должен быть списком словарей")
    else:
        raise TypeError("Тип входного аргумента должен быть списком словарей")

    for dictionary in list_dict:
        state_val = dictionary.get("state")

        if not state_val:
            raise ValueError("В словаре отсутствует информация по статусу state")

        if state_val == state:
            list_res_dict.append(dictionary)

    if not list_res_dict:
        raise ValueError("Отсутствуют словари с указанным статусом 'state'")

    return list_res_dict


def sort_by_date(list_dict: Optional[list[dict]] = None, is_descending: bool = True) -> list[dict]:
    """Функция возвращает новый список, отсортированный по дате (date). На вход принимаются список словарей и
    булевский параметр descending_is (False -сортировка по возрастанию,
    True (по умолчанию)- сортировка производится по убыванию)"""

    sorted_list = []

    if not list_dict:
        raise ValueError("Отсутствует список словарей для сортировки")

    # Проверка типа данных входного аргумента
    if isinstance(list_dict, list):
        for item in list_dict:
            if not isinstance(item, dict):
                raise TypeError("Тип входного аргумента должен быть списком словарей")
            else:
                date_time_str = str(item.get("date", ""))
                if date_time_str:
                    try:
                        datetime.datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M:%S.%f")
                    except ValueError as e:
                        print(f"{str(e)}")
                        raise ValueError("Неверный формат даты")

    else:
        raise TypeError("Тип входного аргумента должен быть списком словарей")

    sorted_list = sorted(list_dict, key=lambda dictionary: str(dictionary.get("date", "")), reverse=is_descending)

    return sorted_list
