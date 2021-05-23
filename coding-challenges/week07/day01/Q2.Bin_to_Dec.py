"""
Write a program to convert Binary number (given as list) to decimal
Integer

Input: [1,0,1]
Output: 5
"""

def Convert_Binary_to_Decimal(list):
    value = 0
    for i in range(len(b_num)):
	    digit = b_num.pop()
	    if digit == '1':
		    value = value + pow(2, i)
    print("The decimal value of the number is", value)
b_num = list(input("Input a binary number: "))
Convert_Binary_to_Decimal(b_num)


#Time Complexity O(n)

#Space Complexity: O(n)