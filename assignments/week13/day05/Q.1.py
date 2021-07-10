"""
Q-1 ) Pascal's Triangle (5 marks)
https://leetcode.com/problems/pascals-triangle/
(5 marks)
(Easy)
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it
as shown:
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:
Input: numRows = 1
Output: [[1]]
"""


class Solution:
    def generate(self, num: int):
        pasc = []
        c = 0
        while num > 0:
            if c == 0:
                pasc.append([1])
                num -= 1
                c += 1
            elif c == 1:
                pasc.append([1,1])
                num -= 1
                c += 1
            else:
                l = [1]
                for i in range(1, len(pasc[-1])):
                    l.append(pasc[-1][i-1] + pasc[-1][i])
                l.append(1)
                pasc.append(l)
                num -=1
        return pasc


