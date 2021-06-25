"""
Q-3 )Remove All Adjacent Duplicates In String (5 marks)
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
(Easy)
You are given a string s consisting of lowercase English letters. A duplicate
removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It can
be proven that the answer is unique.
Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are
adjacent and equal, and this is the only possible move. The result of this move is
that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
"""


def removeDuplicates(S):

    if not S:
        return S

    res = [S[0]]
    for curr in S[1:]:     

        if res and curr == res[-1]:
            res.pop()
        else:
            res.append(curr)

    res = ''.join(res)       

    return res


if __name__ == "__main__":

    s = "abbaca"
    ans = removeDuplicates(s)
    print(ans)
