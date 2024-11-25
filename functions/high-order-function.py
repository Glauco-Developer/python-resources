"""
This script demonstrates the use of higher-order functions in Python, where a function 
is passed as an argument to another function.

1. `funcA(x)`:
   - A simple function that takes an argument `x` and returns `x + 1`.

2. `funcB(func, y)`:
   - A higher-order function that takes another function (`func`) and a value (`y`) as arguments.
   - It applies the passed function (`func`) to the value `y` and multiplies the result by 2.
"""

def funcA(x):
    return x + 1

def funcB(func, y):
    return func(y) * 2

result = funcB(funcA, 5)

print(result)
