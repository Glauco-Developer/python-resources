"""
This script defines a function `count_occurrences` to count how many times a specific character 
appears in a given string. It demonstrates the use of a `for` loop and conditional statements 
inside a function.
"""

def count_occurrences(string, character):
    '''Define a function to count occurrences of a character in a string'''
    counter = 0
    for char in string:
        if char == character:
            counter += 1
    return counter

text = "programming in python"
character_to_find = "a"

result = count_occurrences(text, character_to_find)

print(f"The character '{character_to_find}' appears {result} times in the string.")
