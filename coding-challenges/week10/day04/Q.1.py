
"""
Q-1 ) Valid Parentheses:
https://leetcode.com/problems/valid-parentheses/
(5 marks)
(Easy)
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
Example 1:
Input: s = "()"
Output: true
"""


def isValidParentheses(s):
    
    stack = []
    temp = {"(":")","{":"}","[":"]"}

    for char in s:

        if char in temp:
            stack.append(char)
        elif stack:
            if temp[stack.pop()] != char:
                return False
        else:
            return False

    return len(stack) == 0


if __name__ == "__main__":

    s = []
    ans = isValidParentheses(s)
    print(ans)




