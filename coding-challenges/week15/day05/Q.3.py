
"""
Q-3) Partition Equal Subset Sum
(5Marks)
(Medium)
https://leetcode.com/problems/partition-equal-subset-sum/
Given a non-empty array nums containing only positive integers, find if the array
can be partitioned into two subsets such that the sum of elements in both
subsets is equal.
Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution:
    def canPartition(self, nums) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        target = total//2
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for val in range(target,num-1,-1):
                dp[val] = dp[val] or dp[val-num]
        return dp[-1]

