# List of email addresses
e-mail_list = ['glauco@a.com', 'glauco@b.com', 'glauco@c.com']
print(e-mail_list)  # Print the email list

# Splitting a sentence into words
sentence = "Learn python is fun"
words = sentence.split()  # Split based on spaces
print(words)  # Output: ['Learn', 'python', 'is', 'fun']

# Splitting a sentence based on commas
sentence2 = "Learn,python,is,fun"
words2 = sentence2.split(',')  # Split based on commas
print(words2)  # Output: ['Learn', 'python', 'is', 'fun']

# Joining words into a sentence
sentence3 = ['Learn', 'python', 'is', 'fun']
text = " ".join(sentence3)  # Join with spaces
print(text)  # Output: "Learn python is fun"

# Input names separated by spaces and process them
entrada = input('Enter names separated by spaces: ')
nomes = entrada.split()  # Split input into a list of names

# Greet each name
for nome in nomes:
    print(f'Hello {nome}')

# Join names with hyphens
nomes_hifen = "-".join(nomes)
print(nomes_hifen)  # Example output: "Name1-Name2-Name3"

# Remove duplicates from a list after stripping spaces
lista_palavras = ['Glauco', 'Glauco ', 'Jo', 'Heitor', 'Henrique']
palavras_unicas = []

for palavra in lista_palavras:
    palavra_strip = palavra.strip()  # Remove trailing spaces
    if palavra_strip not in palavras_unicas:
        palavras_unicas.append(palavra_strip)  # Add unique words

print(palavras_unicas)  # Output: Unique stripped words

# Demonstrating list operations
L = []  # Create an empty list
grocery = ['Milk', 'Bread', 'Bread']  # Create a grocery list
grocery.insert(1, 'Egg')  # Insert 'Egg' at position 1
print(grocery)  # Output: ['Milk', 'Egg', 'Bread', 'Bread']

print(grocery.count('Bread'))  # Count occurrences of 'Bread'
print(grocery.index('Bread'))  # Find first occurrence index of 'Bread'

toys = ['Doll', 'Car', 'Game']  # Create another list
grocery.extend(toys)  # Extend grocery list with toys
lista3 = grocery + toys  # Concatenate grocery and toys into lista3
print('lista3', lista3)  # Print the concatenated list

lista3.pop()  # Remove the last element
lista3.pop(1)  # Remove element at index 1
lista3[0] = 'banana'  # Replace the first element with 'banana'
print('lista3', lista3)  # Output the modified list

print(grocery)  # Output the original grocery list

# Create lists using list() and range()
users = list()  # Empty list
numbers = list(range(2, 11, 2))  # Create a list of even numbers from 2 to 10
print(numbers)  # Output: [2, 4, 6, 8, 10]

print(len(numbers))  # Length of the list
print(numbers[len(numbers) - 1])  # Last element of the list
