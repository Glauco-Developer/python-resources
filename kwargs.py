"""
This script demonstrates the use of `**kwargs` in Python functions, which allows passing 
a variable number of keyword arguments to a function.

Key Concepts:
1. `**kwargs`:
   - Collects keyword arguments into a dictionary within the function.
   - Enables the function to accept a flexible number of named arguments.

2. Iterating Through `kwargs`:
   - The function uses a `for` loop to iterate through the dictionary created by `kwargs`.
   - Each key-value pair is printed in a formatted string.
"""

# Define a function to process and display keyword arguments
def person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with arbitrary keyword arguments
person(name="Maria", age="30", city="Rio de Janeiro")
