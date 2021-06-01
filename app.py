import addition
import subtraction
import multiplication
import division

print("Welcome to the python calculator, please enter your options:")

print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")

selection = input("Please enter your selection: ")
selection_int = int(selection)
print(selection_int)

first_number = input("Please enter your first number: ")
first_number_int = int(first_number)
print(first_number_int)

second_number = input("Please enter your second number: ")
second_number_int = int(second_number)
print(second_number_int)

if (selection_int == 1):
    result = addition.add(first_number_int, second_number_int)
elif (selection_int == 2):
    result = subtraction.subtract(first_number_int, second_number_int)
elif (selection_int == 3):
    result = multiplication.multiply(first_number_int, second_number_int)
elif (selection_int == 4):
    result = division.divide(first_number_int, second_number_int)

result_str = str(result)
print("Your result: " + result_str)
