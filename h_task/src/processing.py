from typing import Optional


def filter_by_state(list_dict: Optional[list[dict]] = None, state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'),
    а возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению."""
    list_res_dict = []
    if list_dict:
        for dictionary in list_dict:
            state_val = dictionary.get("state", 0)
            if state_val == state:
                list_res_dict.append(dictionary)
    else:
        print("Отсутствует параметр 'list_dict'")

    return list_res_dict


def sort_by_date(list_dict: Optional[list[dict]] = None, is_descending: bool = True) -> list[dict]:
    """Функция возвращает новый список, отсортированный по дате (date). На вход принимаются список словарей и
    булевский параметр descending_is (False -сортировка по возрастанию,
    True (по умолчанию)- сортировка производится по убыванию)"""
    sorted_list = []
    if list_dict:
        sorted_list = sorted(list_dict, key=lambda dictionary: dictionary.get("date", 0), reverse=is_descending)
    else:
        print("Отсутствует параметр 'list_dict'")

    return sorted_list
