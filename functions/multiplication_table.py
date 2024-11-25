"""
This script defines a function `multiplication_table` that prints the multiplication table (from 1 to 10) 
for a given integer. It uses a `for` loop to iterate through numbers 1 to 10 and calculates 
the product for each iteration.
"""
def multiplication_table(numero):
    """Print the multiplication table for a given number."""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Enter an integer: "))
multiplication_table(numero)
