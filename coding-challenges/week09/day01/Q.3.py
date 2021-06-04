"""
Q-3 ) Given a number n, find sum of first n natural numbers:(5 marks)
"""


def findSum(n) :
	sum = 0
	x = 1
	while x <=n :
		sum = sum + x
		x = x + 1
	return sum


n = 7
print(findSum(n))

