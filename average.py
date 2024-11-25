"""
This script demonstrates two functions for calculating averages: `average` and `average2`.

1. `average`:
   - Calculates the average of two numbers.
   - Uses default parameters (`a=100` and `b=50`), allowing it to be called without arguments.
   - Returns the result of `(a + b) / 2`.

2. `average2`:
   - Accepts a variable number of arguments using `*args`.
   - Calculates the average by summing all arguments and dividing by the number of arguments.
   - Provides flexibility to calculate the average of any number of values.
"""

#%% First cel

def average(a=100, b=50):
    """Calculate the average of two numbers."""
    return (a + b) / 2

result = average()
print(result)

#%% Second cel

def average(*args):
    """Calculate the average of a variable number of arguments."""
    return sum(args) / len(args)

result1 = average(10, 20, 30, 40)
result2 = average(5, 10, 15)
print(result1)
print(result2)