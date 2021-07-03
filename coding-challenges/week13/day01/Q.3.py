"""
Q-3)   Pow(x, n) - Solve using DP (5 marks)
https://leetcode.com/problems/powx-n/
(Medium)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0:
            return 0

        if n==0:
            return 1

        if n < 0:
            x = 1.0 / x
            n = -n

        if n==1:
            return x

        if n%2==1:
            return x * self.myPow(x**2, n//2)
        else:
            return self.myPow(x**2, n//2)