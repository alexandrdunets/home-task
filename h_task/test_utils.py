import json

import pytest

from unittest.mock import mock_open, patch
from src.utils import read_file_to_list
#from tests.conftest import json_to_list_input_output


def test_read_file_to_list(read_file_to_list_input_output):
    """Тест на корректное считывание данных из json файла"""

    content = json.dumps(read_file_to_list_input_output)

    mock_file = mock_open(read_data=content)

    with patch('builtins.open', mock_file):
        result = read_file_to_list("operation.json")

    assert result == read_file_to_list_input_output
