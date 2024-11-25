# Python `while` Loop Examples
i = 1
while i < 5:
    print(i)
    i += 1

### `while` Loop with `break`
```python
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1
```
### `while` Loop with `continue`
```python
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
```
### Infinite `while` Loop (with condition to break out)
```python
count = 0
while True:
    print("Loop iteration:", count)
    count += 1
    if count == 5:
        break
```
### Using `while` to iterate over a list
```python
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
```
### Nested `while` Loop
```python
x = 1
while x <= 3:
    y = 1
    while y <= 2:
        print(f"x: {x}, y: {y}")
        y += 1
    x += 1
```
### `while` Loop with `else`
```python
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished.")
```