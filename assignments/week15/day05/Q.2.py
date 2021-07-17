"""
Q-2 ) First Unique Character in a String (5 marks)
https://leetcode.com/problems/first-unique-character-in-a-string/
(Easy)
Given a string s, find the first non-repeating character in it and return its index. If
it does not exist, return -1.
Example 1:
Input: s = "leetcode"
Output: 0
Example 2:
Input: s = "loveleetcode"
Output: 2
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        indexes = []
        for x in alpha:
            if s.count(x)==1:
                indexes.append(s.index(x))
        try:
            return min(indexes)
        except:
            return -1
