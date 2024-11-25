"""
This script defines a function `countdown` that performs a countdown from a given number `n` to 0 using recursion.

Key Concepts:
1. **Recursive Function**:
   - The function calls itself repeatedly, reducing the input `n` by 1 in each step until it reaches 0 or less.

2. **Base Case**:
   - If `n` is less than or equal to 0, the function prints "Fim" (End) and stops the recursion.

3. **Recursive Case**:
   - If `n` is greater than 0, the function prints the current value of `n` and calls itself with `n-1`.
"""

def countdown(n):
    """Perform a countdown from n to 0 using recursion."""
    if n <= 0: 
        print("Fim")
    else:  # Recursive case
        print(n)
        countdown(n - 1)

number = 5
print(f"Countdown from {number}:")
countdown(number)
