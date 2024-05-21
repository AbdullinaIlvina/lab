#zadanie 7
print("----------------------------------------------")
print("zadanie 7")
import unittest
from reverse import reverse

class TestReverseFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse(''), '')

    def test_one_char_string(self):
        self.assertEqual(reverse('a'), 'a')

    def test_palindrome_string(self):
        self.assertEqual(reverse('racecar'), 'racecar')

    def test_non_palindrome_string(self):
        self.assertEqual(reverse('hello'), 'olleh')

    def test_non_string_non_iterable(self):
        with self.assertRaises(TypeError):
            reverse(123)

    def test_non_string_iterable(self):
        with self.assertRaises(TypeError):
            reverse([1, 2, 3])

if __name__ == '__main__':
    unittest.main()

#zadanie 8
print("----------------------------------------------")
print("zadanie 8")
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

#zadanie 9
print("----------------------------------------------")
print("zadanie 9")
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

