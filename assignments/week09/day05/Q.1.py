"""
#  Q - 1 ) Sort Array by Increasing Frequency (5 Marks)
# https://leetcode.com/problems/sort-array-by-increasing-frequency/submissions/
# Given an array of integers nums, sort the array in increasing order based on the
# frequency of the values. If multiple values have the same frequency, sort them in
# decreasing order.
# Return the sorted array.
"""
# Example 1:
# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a
# frequency of 3.



from collections import Counter

def frequencySort(nums):
    d = Counter(nums)
    def check(x):
        return d[x]

    nums.sort(reverse = True)
    nums.sort(key = check)
    return nums

if __name__ == "__main__":

    A = [1,1,2,2,2,3]
    print(frequencySort(A))
