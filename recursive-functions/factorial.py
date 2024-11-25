"""
This script defines a function `factorial` to calculate the factorial of a given number 
using recursion. The factorial of a number `n` is the product of all positive integers 
from 1 to `n`.

Key Concepts:
1. **Base Case**:
   - The function stops recursing when `n` is 0 or 1, returning 1 as the factorial of 0 or 1 is 1.

2. **Recursive Case**:
   - For `n > 1`, the function calls itself with `n - 1` and multiplies `n` by the result.

3. **Recursion**:
   - The function repeatedly calls itself, reducing the problem size with each call, until it reaches the base case.
"""

def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 8
print(f"The factorial of {number} is {factorial(number)}")
