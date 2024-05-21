import pytest
from reverse import reverse

def test_reverse_empty_string():
    assert reverse("") == ""

def test_reverse_single_character_string():
    assert reverse("a") == "a"

def test_reverse_long_string():
    assert reverse("hello world") == "dlrow olleh"

def test_reverse_lowercase_and_uppercase_characters():
    assert reverse("Hello World") == "dlroW olleH"

def test_reverse_special_characters():
    assert reverse("!@$%^&*()") == ")(*&^%$@!"

def test_reverse_numbers():
    assert reverse("12345") == "54321"
