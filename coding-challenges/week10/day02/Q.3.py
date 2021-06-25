"""
Q-3 ) Longest Common Prefix:
https://leetcode.com/problems/longest-common-prefix/submissions/
(5 marks)
Write a function to find the longest common prefix str amongst an array of
strings.
If there is no common prefix, return an empty str "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""


def longestCommonPrefix(strs):

    if not strs:
        return ""

    newStr = sorted(strs)
    for i in range(len(newStr[0])):

        for str in (newStr[1:]):

            if (str[i] != newStr[0][i]) or (i >= len(str)):
                return newStr[0][:i]

    return newStr[0]


if __name__ == "__main__":

    strs = ["flower","flow","flight"]
    ans = longestCommonPrefix(strs)
    print(ans)
