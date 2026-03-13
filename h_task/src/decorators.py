from functools import wraps
from typing import Optional


def log(filename: Optional[str] = None):
    """Декоратор логирует имя функции и результат выполнения при успешной операции, а также
    имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {str(e)}")
                raise Exception(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")

            else:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")

            return result

        return wrapper

    return decorator
