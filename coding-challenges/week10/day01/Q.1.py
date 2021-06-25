"""
Q-1 ) Number of Good Pairs: (5 marks)
https://leetcode.com/problems/number-of-good-pairs/
Easy
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""




def GoodPairs(nums):
    dic = {}
    count = 0
    for num in nums:

        if num not in dic:
            dic[num] = 1
        elif num in dic:
            count += dic[num]
            dic[num] += 1
            
    return count


if __name__ == "__main__":

    nums = [1,2,3,1,1,3]
    ans = GoodPairs(nums)
    print(ans)
    

