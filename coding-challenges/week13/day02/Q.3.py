
"""
Q-3 ) Longest Common Subsequence - Solve using DP
(5 marks)
https://leetcode.com/problems/longest-common-subsequence/
(Medium)
Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with
some characters (can be none) deleted without changing the relative order of the
remaining characters.
● For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both
strings.
Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is
3
"""


class Solution:

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:

        m = len(s1)
        n = len(s2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.helper(s1, s2, 0, 0, memo)

    def helper(self, s1, s2, i, j, memo):

        if memo[i][j] < 0:
            if i == len(s1) or j == len(s2):
                memo[i][j] = 0
            elif s1[i] == s2[j]:
                memo[i][j] = 1 + self.helper(s1, s2, i + 1, j + 1, memo)
            else:
                memo[i][j] = max(
                    self.helper(s1, s2, i + 1, j, memo),
                    self.helper(s1, s2, i, j + 1, memo),
                )

        return memo[i][j]


if __name__ =="__main__":
    ans = Solution
