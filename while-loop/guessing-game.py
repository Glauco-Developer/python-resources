secret = "python3"
max_tries = 3
tries = 1

while True:
    guess = input("Guess a word: ")
    if guess == secret:
        print("You got it!")
        break
    else:
        print("Incorrect guess. Try again.")
        print("You tried to guess", tries, "times")
        if tries == max_tries:
            print("You ran out of tries.")
            break
        tries += 1