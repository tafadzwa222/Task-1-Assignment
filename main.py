# Program to find the largest of three numbers
print("Enter three numbers to find the largest one:")

# Accepting my input from users
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Finding the largest number using max function
largest = max(num1, num2, num3)

# Displaying the result
print("The largest number among {num1}, {num2}, and {num3} is: {largest}")
