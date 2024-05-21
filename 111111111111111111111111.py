#zadanie 1
print("----------------------------------------------")
print("zadanie 1")
def is_palindrome(data):
    pass

def test_is_palindrome():
    test_cases = [
        ("mach", True),
        ("abat", False),
        ("oko", True),
        ("okno", True),
        ("ivi", True),
    ]
    
    for data, expected in test_cases:
        result = is_palindrome(data)
        if result != expected:
            return False
    return True

if test_is_palindrome():
    print("YES")
else:
    print("NO")


#zadanie 2
print("----------------------------------------------")
print("zadanie 2")
def is_palindrome(data):
    data = data.lower().replace(" ", "")
    return data == data[::-1]


string = input("Введите строку: ")

if is_palindrome(string):
    print("YES")
else:
    print("NO")

#zadanie 3
print("----------------------------------------------")
print("zadanie 3")
import re

def is_correct_mobile_phone_number_ru(number):
    pass

def test_is_correct_mobile_phone_number_ru():
    test_cases = ["+79991234567", "8(999)1234567", "+7 999 123-45-67", "1234567890", "+7(123)4567890"]
    expected_results = [True, True, True, False, False]

    for i in range(len(test_cases)):
        if is_correct_mobile_phone_number_ru(test_cases[i]) != expected_results[i]:
            print("NO")
            return
    print("YES")

test_is_correct_mobile_phone_number_ru()
#zadanie 4
print("----------------------------------------------")
print("zadanie 4")
def is_correct_mobile_phone_ru(phone):
    if len(phone) != 11:
        return False
    if not phone.startswith('8') and not phone.startswith('+7'):
        return False
    if not phone[1:].isdigit():
        return False
    return True

phone_number = input("Enter mobile phone number: ")

if is_correct_mobile_phone_ru(phone_number):
    print("YES")
else:
    print("NO")
#zadanie 5
print("----------------------------------------------")
print("zadanie 5")
def strip_punctuation_ru(data):
    pass


def test_strip_punctuation_ru():
    test_cases = [
        ("Привет, мир!", "Привет мир"),
        ("Как дела?", "Как дела"),
        ("Я люблю программирование!", "Я люблю программирование")
    ]
    
    for data, expected in test_cases:
        result = strip_punctuation_ru(data)
        if result == expected:
            continue
        else:
            print("NO")
            return
    print("YES")

test_strip_punctuation_ru()
#zadanie 6
print("----------------------------------------------")
print("zadanie 6")
def strip_punctuation_ru(data):
    import re
    return ' '.join(re.findall(r'\b\w+\b', data))


data = "Привет, как дела? У меня всё хорошо!"
print(strip_punctuation_ru(data))  


#zadanie 10
print("----------------------------------------------")
print("zadanie 10")
def count_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

s = "hello"
print(count_chars(s))  # Вывод: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

