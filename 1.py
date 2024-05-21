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
