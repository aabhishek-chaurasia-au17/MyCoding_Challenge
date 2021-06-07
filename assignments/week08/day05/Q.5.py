
"""
Q - 5 ) Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.
Example:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Write time and space complexity of your code.
(3 marks)
"""



def findAppear(nums1, nums2):
    repeetNum = []
    for i in nums1:
        if i in nums2:
            repeetNum.append(i)
            nums2.remove(i)
            
    return repeetNum


if __name__=="__main__":

    nums1 = [1,2]
    nums2 = [1,1]
    
    # nums1 = [4,9,5]
    # nums2 = [9,4,9,8,4]

    result = findAppear(nums1, nums2)
    print(result)

