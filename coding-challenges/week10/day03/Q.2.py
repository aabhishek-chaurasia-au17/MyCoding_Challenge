
"""
# Q-2 ) Number of 1 Bits: (5 marks)
# (Medium)
# https://leetcode.com/problems/number-of-1-bits/
# Write a function that takes an unsigned integer and returns the number of '1' bits
# it has (also known as the Hamming weight).
"""
# Example 1:
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has
# a total of three '1' bits.



def Numberof1Bits(n):
    res = 0
    while n:
        res += n & 1
        n >>= 1

    return res


if __name__ == '__main__':

    n = input()
    ans = Numberof1Bits(n)
    print(ans)


