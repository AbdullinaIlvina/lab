import sys
import math

def calculate_args(arg1, arg2, operator):
    try:
        num1 = float(arg1)
        num2 = float(arg2)
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Division by zero error"
        elif operator == '^':
            return math.pow(num1, num2)
        else:
            return "Invalid operator"
    except ValueError:
        return "Invalid input format"

if len(sys.argv) == 4:
    result = calculate_args(sys.argv[1], sys.argv[2], sys.argv[3])
    print(result)
else:
    print("Incorrect number of arguments")
