import sys

if len(sys.argv) == 1:  
    print("NO PARAMS")
else:
    params = sys.argv[1:]  
    result = 0
    coefficient = 1  

    for param in params:  
        try:
            num = int(param) 
            result += num * coefficient
            coefficient *= -1  
        except ValueError:  
            print(ValueError.__name__)  

    print(result)
