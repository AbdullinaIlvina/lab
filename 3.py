number1 = "+7(900)1234567"
number2 = "+7 999 123-45-67"
number3 = "8 925 4567890"
number4 = "79234567890"
number5 = "+7923-456-7890"
number6 = "800-555-3535"

def test_is_correct_mobile_phone_number_ru():
    test_cases = [number1, number2, number3, number4, number5, number6]
    expected_results = [True, True, True, True, False, False]
    
    for i in range(len(test_cases)):
        result = is_correct_mobile_phone_number_ru(test_cases[i])
        if result == expected_results[i]:
            continue
        else:
            print("NO")
            return
    print("YES")

test_is_correct_mobile_phone_number_ru()
