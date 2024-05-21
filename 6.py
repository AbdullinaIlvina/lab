def strip_punctuation_ru(data):
    import re
    return ' '.join(re.findall(r'\b\w+\b', data))


data = "Привет, как дела? У меня всё хорошо!"
print(strip_punctuation_ru(data))  
