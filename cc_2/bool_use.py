# Write a program that takes in 2 numbers and returns true if they are divisible 
# by each other. False otherwise


num1 = int(input("Enter first Value "))
num2 = int(input("Enter second Value "))

result = (bool(num1 % num2 == 0))

print(result)