#problem 1

# Two integer inputs from user
X = int(input("Enter the first integer: "))
Y = int(input("Enter the second integer: "))

# Multiplying the two values
Z = X * Y

# Printing the values of X, Y, and Z
print("X:", X)
print("Y:", Y)
print("Z:", Z)

#problem 2

import sys
# Print the Python version
print("Python version using sys:", sys.version)
import platform
# Print the Python version
print("Python version using platform:", platform.python_version())

#problem 3

help('modules')

#problem 4

print("Value", end="")

#problem 5

# Take an integer input from the user
number = int(input("Enter an integer: "))

# Determine if the number is even or odd
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#problem 6

#without using funtion:
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

# Print original values
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap values
a, b = b, a

# Print swapped values
print("After swapping:")
print("a =", a)
print("b =", b)

#using fuction:
#Function to swap values
def swap_values(x, y):
    return y, x

# Take input for two variables
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

# Print original values
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap the values using the function
a, b = swap_values(a, b)

# Print swapped values
print("After swapping:")
print("a =", a)
print("b =", b)

#problem 7

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print all even numbers in the list
print("Even numbers in the list:")
for number in numbers:
    if number % 2 == 0:
        print(number, end=" ")

#problem 8

# Take a character input from the user
char = input("Enter a character: ").lower()

# Define a set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# Determine if the character is a vowel or not
if char in vowels and len(char) == 1:
    print("The character is a vowel.")
else:
    print("The character is not a vowel.")

#problem 9

# Take a filename input from the user
filename = input("Enter the filename: ")

# Split the filename to get the extension
extension = filename.split(".")[-1]

# Print the extension
print("The extension of the file is:", extension)

#problem 10

# Take a string input from the user
input_string = input("Enter a string: ")

# Take a character input from the user
char_to_count = input("Enter the character to count: ")

# Count the occurrences of the specified character in the string
count = input_string.count(char_to_count)

# Print the number of occurrences
print(f"The character '{char_to_count}' occurs {count} times in the string.")

#problem 11

# Define a list of numbers
numbers = [-3, 7, -2, 0, 9, -1, 4, -5]

# Use a list comprehension to filter positive numbers
positive_numbers = [num for num in numbers if num > 0]

# Print the filtered positive numbers
print("Positive numbers in the list:", positive_numbers)

#problem 12

def find_max_min(numbers):
    if not numbers:
        return None, None  # Return None for both max and min if the list is empty

    # Initialize max and min with the first element of the list
    max_num = numbers[0]
    min_num = numbers[0]

    # Iterate through the list to find max and min
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num

# Example usage:
numbers_list = [5, 3, 9, 1, 7, 2, 4]
max_number, min_number = find_max_min(numbers_list)
print(f"The maximum number is: {max_number}")
print(f"The minimum number is: {min_number}")

#problem 13

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count, odd_count = count_even_odd(numbers_list)

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

#problem 14

# Function to sort numbers in ascending and descending order
def sort_numbers(numbers):
    # Sort in ascending order and store in a new list
    ascending_order = sorted(numbers)
    
    # Sort in descending order and store in a new list
    descending_order = sorted(numbers, reverse=True)
    
    return ascending_order, descending_order

# Example usage:
numbers_list = [5, 2, 9, 1, 7, 3, 4]
ascending, descending = sort_numbers(numbers_list)

# Print the sorted lists
print("Original list:", numbers_list)
print("Ascending order:", ascending)
print("Descending order:", descending)

#problem 15

def find_longest_shortest_words(text):
    # Split the input text into words
    words = text.split()

    if not words:
        return None, None

    # Initialize variables to store longest and shortest words
    longest_word = words[0]
    shortest_word = words[0]

    # Iterate through the list of words to find longest and shortest
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
        if len(word) < len(shortest_word):
            shortest_word = word

    return longest_word, shortest_word

# Example usage:
input_text = input("Enter a line of text: ")
longest, shortest = find_longest_shortest_words(input_text)

# Print the results
if longest and shortest:
    print(f"The longest word is '{longest}' with length {len(longest)}")
    print(f"The shortest word is '{shortest}' with length {len(shortest)}")
else:
    print("No words found.")

#problem 16

def find_largest_smallest(numbers):
    if not numbers:
        return None, None  # Return None for both max and min if the list is empty
    
    # Initialize variables to store largest and smallest numbers
    largest_num = numbers[0]
    smallest_num = numbers[0]

    # Iterate through the list to find largest and smallest numbers
    for num in numbers:
        if num > largest_num:
            largest_num = num
        if num < smallest_num:
            smallest_num = num

    return largest_num, smallest_num

# Example usage:
numbers_list = [5, 2, 9, 1, 7, 3, 4]
largest, smallest = find_largest_smallest(numbers_list)

# Print the results
print("List of numbers:", numbers_list)
print("Largest number:", largest)
print("Smallest number:", smallest)

#problem 17 

def remove_elements_at_positions(input_list, positions):
    # Sort positions in descending order to avoid index shift issues
    positions.sort(reverse=True)
    
    # Remove elements at specified positions
    for pos in positions:
        if pos < len(input_list):
            input_list.pop(pos)

    return input_list

# Example usage:
original_list = [1, 2, 3, 4, 5, 6]
positions_to_remove = [0, 4, 5]

modified_list = remove_elements_at_positions(original_list, positions_to_remove)

# Print the modified list
print("Original list:", original_list)
print("Modified list after removing elements at specified positions:", modified_list)

#problem 18

def print_odd_indices_values(input_list):
    # Iterate through the indices of the list
    for i in range(1, len(input_list), 2):
        print(input_list[i])

# Example usage:
values_list = [10, 20, 30, 40, 50, 60, 70]
print("Values at odd indices:")
print_odd_indices_values(values_list)

#problem 19

#Sorting by value::::::::::
#Ascending order:
def sort_dict_by_value_ascending(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1]))
    return sorted_dict

# Example usage:
my_dict = {'b': 3, 'a': 1, 'c': 2}
sorted_dict_asc = sort_dict_by_value_ascending(my_dict)
print("Sorted dictionary by value (ascending):", sorted_dict_asc)

Descending order:
def sort_dict_by_value_descending(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

# Example usage:
my_dict = {'b': 3, 'a': 1, 'c': 2}
sorted_dict_desc = sort_dict_by_value_descending(my_dict)
print("Sorted dictionary by value (descending):", sorted_dict_desc)

#Sorting by key :::::::::::
#Ascending order:
def sort_dict_by_key_ascending(input_dict):
    sorted_dict = dict(sorted(input_dict.items()))
    return sorted_dict

# Example usage:
my_dict = {'b': 3, 'a': 1, 'c': 2}
sorted_dict_asc = sort_dict_by_key_ascending(my_dict)
print("Sorted dictionary by key (ascending):", sorted_dict_asc)

#Descending order
def sort_dict_by_key_descending(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), reverse=True))
    return sorted_dict

# Example usage:
my_dict = {'b': 3, 'a': 1, 'c': 2}
sorted_dict_desc = sort_dict_by_key_descending(my_dict)
print("Sorted dictionary by key (descending):", sorted_dict_desc)

#problem 20
#Using update() Method
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Make a copy of dict1 to preserve it
    merged_dict.update(dict2)   # Update with dict2
    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = merge_dicts(dict1, dict2)
print("Merged dictionary:", merged_dict)

#problem 21

def search_dict(dictionary, target_value):
    # Iterate through key-value pairs in the dictionary
    for key, value in dictionary.items():
        if value == target_value:
            return key  # Return the key if target_value is found in the dictionary values
    
    return None  # Return None if target_value is not found in the dictionary values

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}

target = 2
result_key = search_dict(my_dict, target)

if result_key:
    print(f"The target value '{target}' was found in the dictionary with key '{result_key}'.")
else:
    print(f"The target value '{target}' was not found in the dictionary.")


