"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For
example, 121 is palindrome while 123 is not.
"""
# Example 1:
# Input: x = 121
# Output: true

# Example 2:
# Input: x = -121
# Output: false
"""
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.
"""


def isPalindrome(n):
    return n == n[::-1]


if __name__ == '__main__':
    n = "121"
    ans = isPalindrome(n)

    if ans:
        print(True)
    else:
        print(False)