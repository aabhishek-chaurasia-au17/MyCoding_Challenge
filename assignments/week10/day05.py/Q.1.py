"""
Q-1 ) Given a list, Write a brute force approach without using stacks(using
for loops, so that you can appreciate the beauty of stacks) to find the just
larger element on the right of the element, for each element.
And for last element, since there is no element on the right give “None”:
(5 marks)
(Easy)
Example 1:
Input: [2,1,7,4,6,8,1,9]
Output: [7,7,8,6,8,9,9,None]
"""


def findMaxElm(nums):

    maxNum = []
    for i in range(0, len(nums)):

        if nums[i] == nums[len(nums) - 1]:
            maxNum.append(None)

        else:
            for j in range(i + 1, len(nums)):

                if nums[j] > nums[i]:
                    maxNum.append(nums[j]) 
                    break

    return maxNum


if __name__ == "__main__":

    nums = [2,1,7,4,6,8,1,9]
    ans = findMaxElm(nums)
    print(ans)

