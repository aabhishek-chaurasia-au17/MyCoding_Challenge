
"""
Q-1 ) Write a program to convert a string of binary number into a decimal
number: (5 marks)
(Easy)
"""
# eg:
# Sample Input
# st = “101”
# Sample output
# 5
# Revise the lecture to see the algorithm to convert binary to decimal



def binaryToDecimal(binary):
	value = 0
	i = 0
	while(binary != 0):

		dec = binary % 10
		value = value + dec * pow(2, i)
		binary = binary // 10
		i += 1

	print(value)	
	


if __name__ == '__main__':

	binaryToDecimal(101)


