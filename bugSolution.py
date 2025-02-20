def function_with_uncommon_error_solution(a, b):
    if b == 0:
        if a == 0:
            return 0 #handle 0/0 case
        elif a > 0:
            return float('inf')
        else:
            return float('-inf')
    else:
        return a / b

result = function_with_uncommon_error_solution(10, 0) #Testing with zero denominator
result2 = function_with_uncommon_error_solution(0,0) #Testing 0/0 case
result3 = function_with_uncommon_error_solution(-10,0) #Testing negative divided by zero case
print(result, result2, result3)