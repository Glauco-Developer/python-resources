"""
This script calculates the number of even numbers from 1 up to a user-specified number (inclusive).
It iterates through each integer in the range and checks whether the number is even using the modulo operator.
The count of even numbers is then displayed.
"""

number = int(input("Enter a number: "))
even_counter = 0

# Loop through numbers from 1 to the entered number (inclusive)
for n in range(1, number + 1):
    if n % 2 == 0:
        even_counter += 1

print(f"There are {even_counter} even numbers.")
