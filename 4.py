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
