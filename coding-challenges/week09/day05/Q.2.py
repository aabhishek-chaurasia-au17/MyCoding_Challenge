"""
Q-2 ) Reverse String:(5 marks) (easy)
Write a function that reverses a string. The input string is given as an array of characters
s.
https://leetcode.com/problems/reverse-string/
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""





def reverseString(str):
    
    if not str or len(str) <= 1:
        return str
    
    left = 0
    right = len(str)-1
    
    while left < right:
        str[left], str[right] = str[right], str[left]
        left += 1
        right -= 1
    return str


if __name__ == "__main__":

    s = ["h","e","l","l","o"]
    res = reverseString(s)
    print(res)



