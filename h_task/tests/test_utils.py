import json

from unittest.mock import mock_open, patch
from src.utils import read_file_to_list


def test_read_file_to_list(capsys, read_file_to_list_input_output):
    """Тест на корректное считывание данных из json файла"""

    content = json.dumps(read_file_to_list_input_output)
    mock_file = mock_open(read_data=content)

    with patch("builtins.open", mock_file):
        result = read_file_to_list("operations.json")

    captured = capsys.readouterr()
    assert captured.out == "Считывание файла: успешно\n"
    assert result == read_file_to_list_input_output


def test_read_file_to_list_empty_file(capsys):
    """Тест на пустой файл"""

    mock_file = mock_open(read_data=None)

    with patch("builtins.open", mock_file):
        result = read_file_to_list("operations.json")

    captured = capsys.readouterr()
    assert captured.out == "Данный файл пустой!\n"
    assert result == []


def test_read_file_to_list_not_list(capsys):
    """Файл содержит не список"""

    content = json.dumps({"a": 1})
    mock_file = mock_open(read_data=content)

    with patch("builtins.open", mock_file):
        result = read_file_to_list("operations.json")

    captured = capsys.readouterr()
    assert captured.out == "Данные по транзакциям должны быть оформлены в виде списка\n"
    assert result == []


def test_read_file_to_list_empty_list(capsys):
    """Тест на пустой список"""

    content = json.dumps([])
    mock_file = mock_open(read_data=content)

    with patch("builtins.open", mock_file):
        result = read_file_to_list("operations.json")

    captured = capsys.readouterr()
    assert captured.out == "Список транзакций пуст!\n"
    assert result == []


def test_read_file_to_list_wrong_file(capsys):
    """Тест на отсутствие файла или некорректный путь"""

    result = read_file_to_list("")
    captured = capsys.readouterr()
    assert captured.out == "Файл не найден, проверьте правильность указанного пути.\n"
    assert result == []


def test_read_file_to_list_wrong_json(capsys):
    """Тест на некорректный формат json данных в файле"""

    mock_file = mock_open(read_data='[{"Invalid":}]')

    with patch("builtins.open", mock_file):
        result = read_file_to_list("operations.json")

    captured = capsys.readouterr()
    assert captured.out == "Ошибка декодирования JSON\n"
    assert result == []
