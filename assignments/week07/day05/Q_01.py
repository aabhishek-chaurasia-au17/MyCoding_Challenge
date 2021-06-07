'''Question 1 :
--------------
Given a number N , count number of SET bits (having 1) in binary format of number N.
INPUT - 26
OUTPUT : 3
Explanation :
N = 26 , binary value = 11010 , count of set bits (having value 1) = 3.
HINT : - Make use of bit manipulation concept .
https://leetcode.com/problems/number-of-1-bits/ --- submit here'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1

        return res