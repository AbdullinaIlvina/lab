import pytest
from my_module import count_chars

def test_count_chars_correct_input():
    assert count_chars("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def test_count_chars_empty_string():
    assert count_chars("") == {}

def test_count_chars_non_string_input():
    with pytest.raises(TypeError):
        count_chars(123)

def test_count_chars_symbols_and_numbers():
    assert count_chars("a1b2c3") == {'a': 1, '1': 1, 'b': 1, '2': 1, 'c': 1, '3': 1}
