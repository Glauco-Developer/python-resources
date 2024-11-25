"""
This script defines a function `print_numbers` that prints all integers from 1 up to a given number `n`. 
It demonstrates the use of a `for` loop within a function and how to call the function with a specific argument.
"""

def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

number = 5
print(f"Numbers from 1 to {number}:")
print_numbers(number)
