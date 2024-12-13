# Working with slices and sorting lists
names_list = ['Glauco', 'Joelly', 'Heitor', 'Henrique']
print(names_list[slice(0, 2)])  # Get the first two elements
print(names_list[slice(2, 4)])  # Get the last two elements
print(names_list[slice(0, 3, 2)])  # Get elements at index 0 and 2

names_list.sort()  # Sort the list alphabetically
print(names_list)  # Output sorted list

names_list.reverse()  # Reverse the sorted list
print(names_list)  # Output reversed list

print('sorted', sorted(names_list))  # Display a sorted copy
print('sorted reverse', sorted(names_list, reverse=True))  # Display a reversed sorted copy

# Creating a matrix (2D list) and checking permutations
tabuleiro = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

# Check if two lists are permutations of each other
def are_permutations(L1, L2):
    if len(L1) != len(L2):
        return False
    for item in L1:
        if L1.count(item) != L2.count(item):
            return False
    return True

list1 = [1, 2, 3]
list2 = [3, 2, 1]
list3 = [1, 2, 2]

print(are_permutations(list1, list2))  # True, because they have the same elements
print(are_permutations(list1, list3))  # False, different elements

# Multiply each element of a matrix by a scalar value
def multiply_matrix_scalar(matrix, scalar):
    result = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element * scalar)
        result.append(new_row)
    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

scaled_matrix = multiply_matrix_scalar(matrix, 2)  # Multiply all elements by 2
print(scaled_matrix)  # Output: [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

# Working with slicing a list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[slice(3, 8)])  # Output: [3, 4, 5, 6, 7]
print(numbers[3:8])  # Equivalent slicing
