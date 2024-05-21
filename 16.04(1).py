import sys

def sum_args(arg1, arg2):
    try:
        return int(arg1) + int(arg2)
    except ValueError:
        return 0

if len(sys.argv) == 3:
    result = sum_args(sys.argv[1], sys.argv[2])
    print(result)
else:
    print(0)
