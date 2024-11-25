"""
This script defines a function `reverse_string` that reverses a given string by iterating over it 
and constructing the reversed string character by character. The function demonstrates string manipulation 
using a `for` loop.
"""

def reverse_string(input_string):
    """Reverse a given string."""
    reversed_string = ''
    for char in input_string:
        reversed_string = char + reversed_string
    print("Reversed string:", reversed_string)

word = input("Enter a word to be reversed: ")
reverse_string(word)
