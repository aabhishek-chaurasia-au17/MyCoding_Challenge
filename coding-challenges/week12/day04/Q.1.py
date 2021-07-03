
"""
Q-1 ) Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/
(5 marks)
(Medium)
Given an integer array nums and an integer k, return the kth largest element in
the array.
Note that it is the kth largest element in the sorted order, not the kth distinct
element.
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""


class Solution:

    def findKthLargest(self, nums, k):
        if not nums or not k or k < 0:
            return None

        minheap = []
        for num in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, num)

            else:
                if num > minheap[0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap, num)

        return minheap[0]


