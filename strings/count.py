"""
This script demonstrates the use of the `count()` method in Python to count the occurrences 
of a specific substring within a string.

Key Concepts:
1. **String `count()` Method**:
   - The `count(substring)` method returns the number of non-overlapping occurrences of a substring in the string.
   - The search is case-sensitive.
"""

text = "Python is a high-level, general-purpose programming language"
result = text.count("a")
print(result)
