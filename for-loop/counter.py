# This Python code snippet counts how many even numbers between 2 and 100 (inclusive) are divisible by 6.
counter = 0
for n in range(2, 101, 2):
    if n % 6 == 0:
        counter += 1
print(counter)