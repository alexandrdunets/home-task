import pytest
from src.processing import filter_by_state


def test_filter_by_state_executed(filter_by_state_input, filter_by_state_executed_output):
    """Тестирование фильтрации списка словарей по статусу state="EXECUTED" (по умолчанию)."""
    assert filter_by_state(filter_by_state_input) == filter_by_state_executed_output


def test_filter_by_state_canceled(filter_by_state_input, filter_by_state_canceled_output):
    """Тестирование фильтрации списка словарей по статусу state="CANCELED"."""
    assert filter_by_state(filter_by_state_input, state="CANCELED") == filter_by_state_canceled_output


