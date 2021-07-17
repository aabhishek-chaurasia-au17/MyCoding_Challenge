
"""
Q-1 ) 4Sum
https://leetcode.com/problems/4sum/
(7.5 marks)
(Medium)
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
● 0 <= a, b, c, d < n
● a, b, c, and d are distinct.
● nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""





class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        i = 0
        L = len(nums)
        res = []
        while i < L-3:
            j = i+1
            while j < L-2:
                left = j+1
                right = L-1
                new_target = target-nums[i]-nums[j]
                while left<right:
                    if nums[left]+nums[right] > new_target:
                        right-=1
                    elif nums[left]+nums[right] < new_target:
                        left+=1
                    else:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        temp_left = nums[left]
                        temp_right = nums[right]
                        while(left<right and nums[left]==temp_left):
                            left+=1
                        while(left<right and nums[right]==temp_right):
                            right-=1
                while j < L-3 and nums[j] == nums[j+1]:
                    j+=1
                j+=1
            while i < L-4 and nums[i] == nums[i+1]:
                i+=1
            i+=1
        return res

