"""
Q-2 )Sum of Unique Elements:
https://leetcode.com/problems/sum-of-unique-elements/
(5 marks)
You are given an integer array nums. The unique elements of an array are the elements that appear
exactly once in the array.
Return the sum of all the unique elements of nums.
Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
"""



def sumOfUnique(nums):

    hashDic = {}
    for i in nums:
        if i in hashDic.keys():
            hashDic[i] += 1
        else:
            hashDic[i] = 1

    sum = 0
    for k, v in hashDic.items():
        if v == 1: sum += k
    return sum


if __name__ == "__main__":

    nums = [1,2,3,2]
    ans = sumOfUnique(nums)
    print(ans)



