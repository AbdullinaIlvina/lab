def strip_punctuation_ru(data):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for char in punctuation:
        data = data.replace(char, '')
    return ' '.join(data.split())

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
