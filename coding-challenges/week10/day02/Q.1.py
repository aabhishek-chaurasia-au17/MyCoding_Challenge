"""
Q-1 )Find the Duplicate Number:
https://leetcode.com/problems/find-the-duplicate-number/
(Solve the above using both the approaches discussed in class) and comment on
time
complexity.
:(5 marks)
Given an array of integers nums containing n + 1 integers where each integer is
in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only
constant extra space.
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
"""





# 1st mathod
"""
def findDuplicate(nums):
        count = [0] * (len(nums)+1)
       
        for val in nums:
            count[val] = count[val] + 1
            print(count)
        for i in range(len(count)):
            if count[i] > 1:
                return i
if __name__ == "__main__":
    nums = [1,3,4,2,2]
    ans = findDuplicate(nums)
    print(ans)
"""


# 2nd mathod

def findDuplicate(nums):
    first = nums[0]
    second = nums[nums[0]]
   
    while first != second: 
        first = nums[first]
        second = nums[nums[second]]
    first = 0
    while first != second: 
        first = nums[first] 
        second = nums[second]
    return first

if __name__ == "__main__":

    nums = [1,3,4,2,2]
    ans = findDuplicate(nums)
    print(ans)


# 3nd mathod
# def findDuplicate(self, nums: List[int]) -> int:
#         for index in range(len(nums)):
#             cur = abs(nums[index])
#             if nums[cur] < 0:
#                 return cur
#             nums[cur] *= -1