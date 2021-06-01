# Attempted to do bonus number 2 here

try:
    print(first_number_int)
except CalculatorInputError:
    print("Error! Please enter the input again")


# This is the main assignment:
# I imported the local modules with the functions that add, subtract, multiply, and divide inside them.

import addition
import subtraction
import multiplication
import division

# Python Calculator 

print("Welcome to the python calculator, please enter your options:")

# 4 options

print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")

# User chooses which operation by putting either numbers 1, 2, 3, or 4

selection = input("Please enter your selection: ")
selection_int = int(selection)
print(selection_int)

# User will enter the first number

first_number = input("Please enter your first number: ")
first_number_int = int(first_number)
print(first_number_int)

# User will enter the second number

second_number = input("Please enter your second number: ")
second_number_int = int(second_number)
print(second_number_int)

# If statement to call one of the 4 functions

if (selection_int == 1):
    result = addition.add(first_number_int, second_number_int)
elif (selection_int == 2):
    result = subtraction.subtract(first_number_int, second_number_int)
elif (selection_int == 3):
    result = multiplication.multiply(first_number_int, second_number_int)
elif (selection_int == 4):
    result = division.divide(first_number_int, second_number_int)

# Printing the result/answer

result_str = str(result)
print("Your result: " + result_str)
