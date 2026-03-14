from functools import wraps
from typing import Optional


def log(filename: Optional[str] = None):
    """Декоратор логирует имя функции и результат выполнения при успешной операции, а также
    имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.
    Если параметр filename=file задан, логи записываются в указанный файл, иначе логи выводятся в консоль."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result

            except Exception as e:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator

