"""
This script defines a recursive function `fibonacci` to generate and print the Fibonacci sequence up to a specified number `n`.

Key Concepts:
1. **Fibonacci Sequence**:
   - A sequence of numbers where each number is the sum of the two preceding ones, starting with 0 and 1.
   - The sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...

2. **Recursive Implementation**:
   - The function uses recursion to compute and print the Fibonacci sequence.
   - It stops recursion when the next value in the sequence (`a`) exceeds the given limit (`n`).

3. **Parameters**:
   - `n`: The upper limit of the Fibonacci sequence.
   - `a` and `b`: The two preceding numbers in the sequence, with default values 0 and 1, respectively.

"""

def fibonacci(n, a=0, b=1):
    """Print the Fibonacci sequence up to a given number n."""
    if a > n:  
        return
    print(a, end=" ")
    fibonacci(n, b, a + b)  # Recursive case: Update a and b

numero = 13
fibonacci(numero)
