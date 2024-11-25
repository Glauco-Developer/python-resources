"""
This script demonstrates the use of `*args` in Python functions, which allows passing a variable 
number of positional arguments to a function.

Key Concepts:
1. `*args`:
   - Collects multiple positional arguments into a tuple within the function.
   - Enables the function to handle an arbitrary number of inputs.

2. Summing the Arguments:
   - The function uses Python's built-in `sum()` function to calculate the total of all values in `args`.
"""

def somatorio(*args):
    return sum(args)

result = somatorio(10, 20, 30, 40, 20)
print(result)
