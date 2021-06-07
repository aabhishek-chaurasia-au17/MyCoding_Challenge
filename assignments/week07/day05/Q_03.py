'''Q3.
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        i = nums.index(target)
        j = i
        for x in range(i+1, len(nums)):
            if nums[x]!=target:
                break
            j = x
        return [i, j]