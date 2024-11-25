"""
This script defines a function `summing` that calculates the sum of all integers from 1 to a given number `n` using recursion.

Key Concepts:
1. **Recursive Function**:
   - The function repeatedly calls itself with a smaller input until it reaches the base case.

2. **Base Case**:
   - If `n` is 0, the function returns 0, which stops the recursion.

3. **Recursive Case**:
   - If `n` is greater than 0, the function returns `n` plus the result of `summing(n-1)`.
"""

def summing(n):
    """Calculate the sum of integers from 1 to n using recursion."""
    if n == 0: 
        return 0
    else:
        return n + summing(n - 1)

numero = 5
resultado = summing(numero)
print(f"The sum of integers from 1 to {numero} is: {resultado}")
