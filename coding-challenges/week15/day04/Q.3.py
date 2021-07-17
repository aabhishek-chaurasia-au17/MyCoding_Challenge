
"""
Q-3) Minimum Operations to Reduce X to Zero (5 marks)
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
(Medium)
You are given an integer array nums and an integer x. In one operation, you can
either remove the leftmost or the rightmost element from the array nums and
subtract its value from x. Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it is
possible, otherwise, return -1.
Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x
to zero
"""

class Solution:
    def minOperations(self, nums, x: int) -> int:
        if x == 0:
            return 0
        if min(nums)>x:
            return -1
        x_ = sum(nums)-x
        if x_==0:
            return len(nums)
        if x_<0:
            return -1
        
        start = 0
        max_len = 0
        tmp_sum = 0
        for end in range(len(nums)):
            tmp_sum += nums[end]
            if tmp_sum>x_:
                while tmp_sum >x_:
                    tmp_sum-=nums[start]
                    start+=1
            if tmp_sum == x_:
                max_len = max(max_len, end-start+1)
        return len(nums)-max_len

