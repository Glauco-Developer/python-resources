# Python `for` Loop Examples

```python
# Basic `for` Loop
for _ in range(4):
    print("Python")

# `for` Loop with Step
for x in range(2, 30, 3):
    print(x)

# `for` Loop with `else`
for i in range(4):
    print(i)
else:
    print("For Finished")

# Nested `for` Loop
for i in range(3):
    for j in range(2):
        print(i, j)

# Iterating over a String
for character in "Python":
    print(character)

# Using `enumerate` in a `for` Loop
for i, character in enumerate("Python"):
    print(f'{i} -> {character}')

# `for` Loop with `break`
for i in range(10):
    if i == 5:
        print("Breaking at", i)
        break
    print(i)

# `for` Loop with `continue`
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
