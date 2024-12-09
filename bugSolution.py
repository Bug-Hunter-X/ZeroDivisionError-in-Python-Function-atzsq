def my_function(x):
    try:
        if x == 0:
            return 0
        else:
            return 1 / x
    except ZeroDivisionError:
        return float('inf')

print(my_function(0)) # Output: inf
print(my_function(5)) # Output: 0.2