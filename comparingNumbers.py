# This script compares two numbers entered by the user

# Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers and print the result
if num1 > num2:
    print("The first number is greater than the second number.")
elif num1 < num2:
    print("The first number is less than the second number.")
else:
    print("Both numbers are equal.")
