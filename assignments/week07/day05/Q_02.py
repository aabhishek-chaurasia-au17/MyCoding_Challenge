'''
Question : 2 - https://leetcode.com/problems/sqrtx/
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        result = 0 
        left = 1
        right = x/2
        while left <= right:
            mid = math.floor((left+right)/2)
            if mid * mid > x:
                right = mid - 1
            else:
                result = mid
                left = mid + 1
        return result