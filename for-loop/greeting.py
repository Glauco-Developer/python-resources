"""
This script takes a user input of space-separated names and greets each name individually.
It processes the input character by character, constructing each name until a space is encountered,
at which point it prints a personalized greeting and resets for the next name. Any leftover name
after the loop is also greeted.

Usage:
1. Run the script.
2. Enter names separated by spaces when prompted.
3. The script will print "Hi" followed by each name.
"""

# Prompt the user to input names separated by spaces
names = input("Enter with separated names by spaces: ")

# Initialize an empty string to build each name
name = ""

# Loop through each character in the input string
for char in names:
    if char != " ":  # If the character is not a space, add it to the current name
        name += char
    else:
        print("Hi", name)  # Print greeting for the complete name
        name = ""  # Reset name for the next one

# Print greeting for the last name if there's any leftover
if name:
    print("Hi", name)
