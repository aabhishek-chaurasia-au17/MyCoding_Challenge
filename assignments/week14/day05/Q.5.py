
"""
Q-5) [BONUS QUESTION] Search a 2D Matrix (3.75 marks)
(Medium)
https://leetcode.com/problems/search-a-2d-matrix/
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
● Integers in each row are sorted from left to right.
● The first integer of each row is greater than the last integer of the
previous row.
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""





class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        
        start = 0
        end = len(matrix)
        
        if end == 0:
            return False
        
        while start < end:
            mid = (start + end) // 2
            
            s = 0
            e = len(matrix[mid])
        
            if e == 0:
                return False
            
            while s < e:
                m = (s+e)//2
                
                if matrix[mid][m] == target:
                    return True
                elif matrix[mid][m] < target:
                    s = m + 1
                else:
                    e = m
            
            if matrix[mid][0] > target:
                end = mid
            elif matrix[mid][-1] < target:
                start = mid + 1
            else:
                return False
        return False