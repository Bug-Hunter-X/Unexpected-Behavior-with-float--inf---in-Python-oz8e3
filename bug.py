def function_with_uncommon_error(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return float('inf')  # This might cause issues with further calculations 
    else:
        return a / b

result = function_with_uncommon_error(10, 0)