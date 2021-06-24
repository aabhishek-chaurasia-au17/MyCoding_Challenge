"""
Q-4 ) [Bonus Question] Move Zeroes: (5 extra marks) (Medium)
https://leetcode.com/problems/move-zeroes/
Given an integer array nums, move all 0's to the end of it while maintaining the relative
order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


def MoveZeroes(nums):
    left = 0
    right = 0
    while right < len(nums):
        if nums[left] == 0:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            else:
                right += 1
        else:
            left += 1
            right += 1
    return nums


if __name__ == "__main__":

    nums = [0,1,0,3,12]
    res = MoveZeroes(nums)
    print(res)
