"""
Q-2 ) Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
(5 marks)
You are given two integer arrays nums1 and nums2, sorted in
non-decreasing order, and two integers m and n, representing the number
of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing
order.
The final sorted array should not be returned by the function, but instead
be stored inside the array nums1. To accommodate this, nums1 has a
length of m + n, where the first m elements denote the elements that should
be merged, and the last n elements are set to 0 and should be ignored.
nums2 has a length of n.
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming
from nums1.

"""
class Solution:
    def merge(self, nums1, m,nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        i, j = m - 1, n -1
        while last >= 0:
            if j < 0 or (i >= 0 and nums1[i] >= nums2[j]):
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1
        return nums1

