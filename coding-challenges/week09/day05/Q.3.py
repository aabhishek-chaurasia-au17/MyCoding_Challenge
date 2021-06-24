"""
Q-3 )Maximum Ascending Subarray Sum: (5 marks) (easy)
https://leetcode.com/problems/maximum-ascending-subarray-sum/
Given an array of positive integers nums, return the maximum possible sum of an
ascending subarray in nums.
A subarray is defined as a contiguous sequence of numbers in an array.
A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where left <= i < right,
numsi < numsi+1. Note that a subarray of size 1 is ascending.
Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
"""





def MaxAscendingSum(nums):
    count = nums[0]
    maxSum = nums[0]

    for i in range(1, len(nums)):

        if nums[i] > nums[i-1]:
            count += nums[i]
        else:
            count = nums[i]
        maxSum = max(maxSum, count)

    return maxSum


if __name__ == "__main__":

    nums = [10,20,30,5,10,50]
    res = MaxAscendingSum(nums)
    print(res)


