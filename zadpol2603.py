print("----------------------------------------------------")
print("Zadanie 1")
password = input("Введите пароль: ")


if len(password) < 8:
    print("error")

elif not any(char.isupper() for char in password):
    print("error")

elif not any(char.islower() for char in password):
    print("error")

elif not any(char.isdigit() for char in password):
    print("error")

elif any((password[i:i+3]).lower() in ['qwe', 'йцу', 'tyu', 'нгш', 'asd', 'фыв', 'zxc', 'ячс', '123', '123456', 'йцукен'] for i in range(len(password)-2)):
    print("error")
else:
    print("ok")


print("----------------------------------------------------")
print("Zadanie 2")
class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

class SequenceError(PasswordError):
    pass

def check_password(password):
    if len(password) < 9:
        raise LengthError("Длина пароля должна быть не менее 9 символов")
    if password.islower() or password.isupper():
        raise LetterError("Пароль должен содержать сочетание прописных и строчных букв")
    if not any(char.isdigit() for char in password):
        raise DigitError("Пароль должен содержать хотя бы одну цифру")
    if any((password[i:i+3]).lower() in ['qwe', 'йцу', 'tyu', 'нгш', 'asd', 'фыв', 'zxc', 'ячс', '123', '123456', 'йцукен'] for i in range(len(password)-2)):
        raise SequenceError("Пароль не должен содержать последовательности символов")

    return "ok"

try:
    password = input("Введите пароль: ")
    result = check_password(password)
    print(result)
except PasswordError as pe:
    print(f"Ошибка: {pe}")


print("----------------------------------------------------")
print("Zadanie 3")
def check_password(password):
    try:
        assert len(password) >= 8, "Пароль должен содержать не менее 8 символов"
        assert any(char.isdigit() for char in password), "Пароль должен содержать хотя бы одну цифру"
        assert any(char.isalpha() for char in password), "Пароль должен содержать хотя бы одну букву"
        assert any(not char.isalnum() for char in password), "Пароль должен содержать хотя бы один специальный символ"
        print("ok")
    except AssertionError as e:
        print(f"ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


password1 = "Abc12345"
password2 = "12345678"
password3 = "Abcdefgh"
password4 = "1234HHHDyt56ksdew78$"

check_password(password1)  
check_password(password2)  
check_password(password3)  
check_password(password4)  

print("----------------------------------------------------")
print("Zadanie 4")
def validate_password(password):
    if len(password) < 8:
        raise ValueError("Пароль должен быть длиной не менее 8 символов")
    elif not any(char.isdigit() for char in password):
        raise ValueError("Пароль должен содержать хотя бы одну цифру")
    elif not any(char.isalpha() for char in password):
        raise ValueError("Пароль должен содержать хотя бы одну букву")
    elif not any(char.isupper() for char in password):
        raise ValueError("Пароль должен содержать хотя бы одну заглавную букву")
    elif not any(char.islower() for char in password):
        raise ValueError("Пароль должен содержать хотя бы одну строчную букву")
    return True

def main():
    while True:
        try:
            password = input("Введите пароль: ")
            if password.lower() == "ctrl+break":
                print("Имитация нажатия Ctrl+Break.")
                break
            validate_password(password)
            print("Пароль действителен.")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")
    print("Bye-Bye")

if __name__ == "__main__":
    main()
        
print("----------------------------------------------------")
print("Zadanie 5")

class DefaultList(list):
    def __init__(self, default_value):
        self.default_value = default_value
        super().__init__()

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return self.default_value


my_list = DefaultList(default_value=0)
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list[0])  
print(my_list[1])  
print(my_list[2])  
print(my_list[3])  



