"""
Q-1 ) Recursive implementation of atoi() function:                          (5 marks)
Atoi() function converts a string into an integer.
eg:
st = “1234” is a string.
if we perform,
st + 1
this results in error since “st” is a string and 1 is an integer, and,
st + “1”
this will append 1 into 1234. Giving us 12341.
write a function that converts the above variable ‘st’ into an integer (so that we
can perform mathematical operations on it).
Let’s call our function “myAtoiRecursive()”, it should,
myAtoiRecursive(st) + 1
should give us 1235 (that is 1234+1).
"""

def AtoiRecursive(string, num):
	
	if len(string) == 1:
		return int(string) + (num * 10)
		
	num = int(string[0:1]) + (num * 10)
	
	return AtoiRecursive(string[1:], num)

string = "1234"

print(AtoiRecursive(string, 0))

