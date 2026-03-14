import pytest
from src.decorators import log


@log()  # Применяем декоратор log c указанием параметра
def div_to_consol(a, b):
    return a / b


def test_log():
    """Тест на корректную работу исходной функции после декорирования"""
    result = div_to_consol(2, 1)
    assert result == 2


def test_log_consol(capsys):
    """Тест на проверку вывода в консоль сообщения о корректном выполнении исходной функции"""
    div_to_consol(2, 1)
    captured = capsys.readouterr()
    assert captured.out == "div_to_consol ok\n"


def test_log_consol_err(capsys):
    """Тест на проверку возникающего исключения и вывода в консоль сообщения об ошибке"""
    with pytest.raises(Exception, match="division by zero"):
        div_to_consol(2, 0)
        captured = capsys.readouterr()
        assert captured.out == "div_to_consol error: division by zero. Inputs: (2, 0), {}\n"


log_file = "mylog.txt"


@log(filename=log_file)  # Применяем декоратор log c указанием параметра
def div_to_file(a, b):
    return a / b


def test_log_file():
    """Тест на проверку вывода в файл сообщения о корректном выполнении исходной функции"""

    div_to_file(2, 1)

    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            pass
        last_line = line  # Последняя строка в файле
        assert last_line == "div_to_file ok\n"


def test_log_file_err():
    """Тест на проверку вывода в файл сообщения об ошибке выполнения исходной функции"""

    with pytest.raises(Exception):
        div_to_file(2, 0)

    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            pass
        last_line = line  # Последняя строка в файле
        assert last_line == "div_to_file error: division by zero. Inputs: (2, 0), {}\n"
