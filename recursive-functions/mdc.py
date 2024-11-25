"""
This script defines a function `gcd` (Greatest Common Divisor) to calculate the greatest common divisor of two integers using the Euclidean algorithm.

Key Concepts:
1. **Greatest Common Divisor (GCD)**:
   - The largest positive integer that divides two numbers without leaving a remainder.

2. **Euclidean Algorithm**:
   - If `b` is 0, the GCD is `a`.
   - Otherwise, the GCD of `a` and `b` is the same as the GCD of `b` and `a % b` (the remainder when `a` is divided by `b`).
"""

def gcd(a, b):
    """Calculate the greatest common divisor using the Euclidean algorithm."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

number1 = 48
number2 = 18

result = gcd(number1, number2)
print(f"The greatest common divisor of {number1} and {number2} is: {result}")
