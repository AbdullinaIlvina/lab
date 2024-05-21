import sys

arguments = sys.argv[1:]
sort_flag = False
key_value_pairs = {}

if arguments and arguments[0] == '--sort':
    sort_flag = True
    arguments = arguments[1:]

for arg in arguments:
    key, value = arg.split('=')
    key_value_pairs[key] = value

if sort_flag:
    for key in sorted(key_value_pairs.keys()):
        print(f"Key: {key} Value: {key_value_pairs[key]}")
else:
    for key, value in key_value_pairs.items():
        print(f"Key: {key} Value: {value}")
