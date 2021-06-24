"""
Q-1 ) Squares of a Sorted Array:(5 marks) (easy)
https://leetcode.com/problems/squares-of-a-sorted-array/
Given an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order.
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""





def SortedArray(nums):
    n = len(nums)
    i = 0  
    j = n - 1
    k = n - 1
    result = list(range(n)) 

    while i <= j:
        SqrNg = nums[i] * nums[i]
        SqrPo = nums[j] * nums[j]
        if SqrNg < SqrPo:

            result[k] = SqrPo
            j = j - 1
        else:
    
            result[k] = SqrNg
            i = i + 1
        k = k - 1

    return result


if __name__ == "__main__":

    nums = [-4,-1,0,3,10]
    res = SortedArray(nums)
    print(res)



