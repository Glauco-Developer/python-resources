"""
This script is a guessing game where the user attempts to guess how many even numbers 
between a defined range (inclusive) are divisible by 6. The correct number is calculated 
in advance, and the user has a limited number of attempts to guess it. 

Features:
1. Calculates the number of even numbers divisible by 6 within the range.
2. Allows the user three attempts to guess the correct number.
3. Provides feedback ("too low" or "too high") for incorrect guesses.
4. Displays the correct answer if the user exhausts all attempts.
"""

# Define the range
lower_limit = 1
upper_limit = 100

# Calculate the correct number of even numbers divisible by 6 in the range
counter = 0
correct_number = 0
for i in range(lower_limit, upper_limit + 1):
    if i % 2 == 0 and i % 6 == 0:
        counter += 1

correct_number = counter

# Initialize guessing variables
attempts = 0
max_attempts = 3
guessed_correctly = False

# Start the guessing game
while attempts < max_attempts and not guessed_correctly:
    guess = int(input(f"Guess how many even numbers divisible by 6 exist between {lower_limit} and {upper_limit}: "))
    attempts += 1
    if guess == correct_number:
        print("Congratulations! You got it!")
        guessed_correctly = True
    elif attempts < max_attempts:
        if guess < correct_number:
            print("Too low! Try again: ")
        else:
            print("Too high! Try again: ")

# End of the game
if not guessed_correctly:
    print(f"You've run out of attempts. The correct number was {correct_number}.")
