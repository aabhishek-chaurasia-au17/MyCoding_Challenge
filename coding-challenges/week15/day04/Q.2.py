"""
Q-2) Longest Substring Without Repeating Characters (5 marks)
https://leetcode.com/problems/longest-substring-without-repeating-charact
ers/
(Medium)
Given a string s, find the length of the longest substring without repeating
characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        p1 = p2 = m = 0
        
        while p2 < len(s):
            if s[p2] not in d:
                d[s[p2]] = True
                p2 += 1
                m = max(len(d), m)
            else:
                del d[s[p1]]
                p1 += 1
            
        return m

