
"""
Q-2)Letter Combinations of a Phone Number (5 marks)
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
(Medium)
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:
Input: digits = ""
Output: []
"""





class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if digits == "":
            return []
        
        def getChars(d):
            if d == '2':
                return ['a', 'b', 'c']
            elif d == '3':
                return ['d', 'e', 'f']
            elif d == '4':
                return ['g', 'h', 'i']
            elif d == '5':
                return ['j', 'k', 'l']
            elif d == '6':
                return ['m', 'n', 'o']
            elif d == '7':
                return ['p', 'q', 'r', 's']
            elif d == '8':
                return ['t', 'u', 'v']
            elif d == '9':
                return ['w', 'x', 'y', 'z']
                
        array = getChars(digits[0])
        
        if len(digits) == 1:
            return array
        
        for d in digits[1:]:
            chars = getChars(d)
            newArray = []
            for a in array:
                for c in chars:
                    newArray.append(a+c)
            array = newArray
        return array

