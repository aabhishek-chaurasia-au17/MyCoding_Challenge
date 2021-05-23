"""
Question 1 :
----------------
Given a decimal Number , Write a program to convert Decimal to Binary
number.

Input : 10 (decimal)
Output: - 1010
"""

def Decimal_to_Binary(number):
    if number > 1:
        Decimal_to_Binary(number // 2)
    print(number % 2, end='')
number = int(input("Enter any decimal number: "))
Decimal_to_Binary(number)

#Time Complexity O(n)
#Space Complexity: O(n)