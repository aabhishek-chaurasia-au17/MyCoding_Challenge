"""
Q-1 ) Check if a number is Palindrome:                  (5 marks)
Given an integer, write a function that returns true if the given 
number is palindrome, else false.
For example,
Sample input:
12321
Sample output:
palindrome
eg2:
Sample input:
1451
Sample output:
not palindrome.
"""


def oneDigit(num):
	
	return ((num >= 0) and
			(num < 10))

def isPalUtil(num, dupNum):
	
	if oneDigit(num):
		return (num == (dupNum[0]) % 10)

	if not isPalUtil(num //10, dupNum):
		return False

	dupNum[0] = dupNum[0] //10

	return (num % 10 == (dupNum[0]) % 10)

def isPal(num):
	if (num < 0):
		num = (-num)

	dupNum = [num] # *dupNum = num

	return isPalUtil(num, dupNum)

# Driver Code
n = 12321
if isPal(n):
	print("Yes")
else:
	print("No")

n = 1451
if isPal(n) :
	print("Yes")
else:
	print("No")

# This code is contributed by mits
