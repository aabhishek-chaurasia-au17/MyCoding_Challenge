"""
Q-2 )Next Greater Element I: (5 marks)
https://leetcode.com/problems/next-greater-element-i/
(Medium)
(See doubt session recording today to use stack to solve this problem)
You are given two integer arrays nums1 and nums2 both of unique elements,
where nums1 is a subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding
places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to
its right in nums2. If it does not exist, return -1 for this number.
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
For number 4 in the first array, you cannot find the next greater number for it in
the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array
is 3.
For number 2 in the first array, there is no next greater number for it in the
second array, so output -1.
"""


def nextGreaterElmt(nums1, nums2):

    res = []
    stack = []
    mapObj = {}

    for n in nums2:
        while stack and n > stack[-1]:
            mapObj[stack.pop()] = n
        stack.append(n)

    while stack:
        mapObj[stack.pop()] = -1

    for n in nums1:
        res.append(mapObj[n])

    return res


if __name__ == "__main__":

    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    ans = nextGreaterElmt(nums1, nums2)
    print(ans)
