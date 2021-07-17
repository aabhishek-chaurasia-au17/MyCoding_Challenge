
"""
Q-3) Unique Paths III (5 marks)
https://leetcode.com/problems/unique-paths-iii/
(Hard)
On a 2-dimensional grid, there are 4 types of squares:
● 1 represents the starting square. There is exactly one starting square.
● 2 represents the ending square. There is exactly one ending square.
● 0 represents empty squares we can walk over.
● -1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending
square, that walk over every non-obstacle square exactly once.
Example 1:
Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:
Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Marks distribution:
Question 1,2 and 3 carry 5 marks each
"""





class Solution:
    def dfs(self, m, r, c, visited, total_to_visit, rows, cols):
        if not (0 <= r < rows and 0 <= c < cols): return
        if m[r][c] == 2:
            if len(visited) == total_to_visit + 1:
                self.paths += 1
            return
        elif m[r][c] == -1:
            return
        elif (r, c) in visited:
            return
        visited.add((r, c))
        self.dfs(m, r + 1, c, visited, total_to_visit, rows, cols)
        self.dfs(m, r - 1, c, visited, total_to_visit, rows, cols)
        self.dfs(m, r, c + 1, visited, total_to_visit, rows, cols)
        self.dfs(m, r, c - 1, visited, total_to_visit, rows, cols)
        visited.discard((r, c))

    def uniquePathsIII(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        total_to_visit = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    total_to_visit += 1
                if grid[row][col] == 1:
                    x, y = row, col
        self.paths = 0
        self.dfs(grid, x, y, set(), total_to_visit, rows, cols)
        return self.paths

