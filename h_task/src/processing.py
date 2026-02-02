def filter_by_state(list_dict=None, state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'),
       а возвращает новый список словарей, содержащий только те словари, у которых ключ state
       соответствует указанному значению."""

    list_res_dict = []
    for dictionary in list_dict:
        state_val = dictionary.get("state", 0)
        if state_val == state:
            list_res_dict.append(dictionary)
    return list_res_dict


def sort_by_date(list_dict=None, descending: bool = True) -> list[dict]:
    """Функция возвращает новый список, отсортированный по дате (date). На вход принимаются список словарей и
        булевский параметр descending (False -сортировка по возрастанию, True (по умолчанию)- сортировка производится по убыванию)"""
    sorted_list = sorted(list_dict, key=lambda dictionary: dictionary.get("date", 0), reverse=descending)
    return sorted_list
