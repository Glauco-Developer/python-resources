"""
This script defines a function `even_or_odd` that determines whether a given integer is even or odd.
It uses a simple conditional (`if`) statement to check the divisibility of the number by 2 and returns 
the corresponding type ("even" or "odd").
"""

def even_or_odd(n):
    """Check if a number is even or odd."""
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'

number = int(input('Enter an integer: '))
number_type = even_or_odd(number)
print(f"The number you entered is {number_type}.")
