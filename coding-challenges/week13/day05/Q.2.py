"""
Q-2 )Palindrome Number - Try using BFS in this (5 marks)
https://leetcode.com/problems/palindrome-number/
(Easy)
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For
example, 121 is palindrome while 123 is not.
Example 1:
Input: x = 121
Output: true
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.
"""





class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        rev = 0
        temp = x
        while temp > 0:
            rev = (rev * 10) + (temp % 10)
            temp = temp // 10
        return rev == x

