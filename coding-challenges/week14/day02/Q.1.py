
"""
Q-1 ) N-Queens
https://leetcode.com/problems/n-queens-ii/
(5 marks)
(Medium)
The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens
puzzle.
Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:
Input: n = 1
Output: 1
"""





class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        
        def helper(row = 0, diag1 = set(), diag2 = set(), column = set()):
            if row == n:
                self.count += 1
            for col in range(n):
                if row - col not in diag1 and row + col not in diag2 and col not in column:
                    helper(row + 1, diag1.union({row - col}), diag2.union({row + col}), column.union({col}))
        helper()
        return self.count

