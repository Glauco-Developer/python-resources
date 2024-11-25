"""
This script demonstrates various string methods in Python to perform operations and checks on a string.

Key Concepts:
1. **String Methods**:
   - Python provides built-in methods to manipulate strings and perform checks.

2. **Common String Operations**:
   - `upper()`: Converts all characters to uppercase.
   - `lower()`: Converts all characters to lowercase.
   - `capitalize()`: Capitalizes the first character.
   - `swapcase()`: Swaps the case of all characters.
   - `len()`: Returns the length of the string.
   - `startswith()`: Checks if the string starts with a specific substring.
   - `endswith()`: Checks if the string ends with a specific substring.
   - `isalnum()`: Checks if the string contains only alphanumeric characters.
   - `isalpha()`: Checks if the string contains only alphabetic characters.
   - `isdigit()`: Checks if the string contains only digits.
   - `isnumeric()`: Checks if the string contains only numeric characters.
"""
text = "python"

uppercase_text = text.upper()
lower_text = text.lower()
capitalize_text = text.capitalize()
swapped_text = text.swapcase()
length_text = len(text)
starts_with_text = text.startswith("py")
ends_with_text = text.endswith("thon")
isalnum_text = text.isalnum()
isalpha_text = text.isalpha()
isdigit_text = text.isdigit()
isnumeric_text = text.isnumeric()

print(uppercase_text)
print(lower_text)
print(capitalize_text)
print(swapped_text)
print(length_text)
print(starts_with_text)
print(ends_with_text)
print(isalnum_text)
print(isalpha_text)
print(isdigit_text)
print(isnumeric_text)
