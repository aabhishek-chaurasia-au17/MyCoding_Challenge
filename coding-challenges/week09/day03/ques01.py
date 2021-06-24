"""

Q-1 ) Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/submissions/
(5 marks)
Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must be unique and you may return
the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

"""

#  first sol with 90ms
class Solution:
    def intersection(self, nums1, nums2) :
        a = []
        for i in nums1:
            if i in nums2:
                a.append(i)
        a = list(set(a))
        return a

# second sol with witn 24 ms
class Solution:
    def intersection(self, nums1, nums2) :
        return list(set(nums1) & set(nums2))
