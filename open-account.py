"""
This script demonstrates the use of `**kwargs` in Python functions to accept and process 
a variable number of keyword arguments.

Key Concepts:
1. `**kwargs`:
   - Collects keyword arguments into a dictionary within the function.
   - Allows flexibility in the number and names of arguments passed.

2. Formatting the Account Information:
   - Iterates through the dictionary `kwargs.items()` to build a formatted string of key-value pairs.
   - Capitalizes the keys and formats the output as `Key: Value`.

3. Removing Trailing Comma and Space:
   - Removes the last ", " using slicing (`account_info[:-2]`) if the string is not empty.

"""

def open_account(**kwargs):
    """Format and return account details from keyword arguments."""
    account_info = ''
    for key, value in kwargs.items():
        account_info += f"{key.capitalize()}: {value}, "
    # Remove the last comma and space, if present
    if account_info:
        account_info = account_info[:-2]
    return account_info

account_details = open_account(name="Glauco", type="savings", balance="10000000")
print(account_details)
