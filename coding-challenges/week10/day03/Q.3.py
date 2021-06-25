"""
Q-3 )Write a function to perform XOR between two positive integers: (5
marks), do not use the xor operator.
(Easy)
"""
# Sample Input:
# A = 5
# B = 3
# Sample Output:
# A^B = 6
# explanation:
# Take two inputs A and B as integers. => A = 5 , B = 3
# Convert them to binary, => A = 101, B = 011
# perform XOR operation, => A^B = 110
# return resultant binary number as decimal number . => (110)2 = (6)10


def perform_XOR(x, y):
	res = 0 

	for i in range(31, -1, -1):
		
		b1 = x & (1 << i)
		b2 = y & (1 << i)
		b1 = min(b1, 1)
		b2 = min(b2, 1)

		xorOP = 0
		if (b1 & b2):
			xorOP = 0
		else:
			xorOP = (b1 | b2)

		res <<= 1;
		res |= xorOP
	return res

if __name__ == '__main__':

    A = 5
    B = 3
    ans = perform_XOR(A, B)
    print(ans)