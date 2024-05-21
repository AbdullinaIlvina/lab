def is_palindrome(data):
    data = data.lower().replace(" ", "")
    return data == data[::-1]


string = input("Введите строку: ")

if is_palindrome(string):
    print("YES")
else:
    print("NO")
