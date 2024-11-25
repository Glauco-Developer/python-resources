"""
This script defines a function `calculate_total` to calculate the total price of an item, 
including a tip percentage. It demonstrates the use of parameters in a function and how to 
return and use the calculated value.
"""

def calculate_total(price, percent):
    """Calculate total price including tip."""
    total = price + percent * price
    return total

price = 20
percent = 0.10

total_price = calculate_total(price, percent)
print("Total price with tip:", total_price)
