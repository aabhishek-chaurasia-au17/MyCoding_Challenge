
"""
Q-2 ) Tiling a Rectangle with the Fewest Squares - Solve with DP
(5 marks)
(Easy-since we solved it in recursion topic)
https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
Given a rectangle of size n x m, find the minimum number of integer-sided
squares that tile the rectangle.
Example 1:
Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)
Example 2:
Input: n = 5, m = 8
Output: 5
"""


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m: return 1
        depth = [0]*m
        
        def fn(x): 
            nonlocal ans 
            if x < ans: 
                if min(depth) == n: ans = x # all tiled
                else: 
                    i = min(depth)
                    j = jj = depth.index(i) # (i, j)
                    while jj < m and depth[jj] == depth[j]: jj += 1
                    k = min(n - i, jj - j)
                    for kk in reversed(range(1, k+1)): 
                        for jj in range(j, j+kk): depth[jj] += kk
                        fn(x+1)
                        for jj in range(j, j+kk): depth[jj] -= kk
                            
        ans = max(n, m)
        fn(0)
        return ans 


