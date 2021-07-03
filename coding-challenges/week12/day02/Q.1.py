
"""
(Maximum marks -15)
Q-1 ) Print vertical order traversal, or Top view of a binary tree
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
(5 marks)
(Easy)
Given the root of a binary tree, calculate the vertical order traversal of the binary
tree.
For each node at position (row, col), its left and right children will be at positions
(row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0,
0).
The vertical order traversal of a binary tree is a list of top-to-bottom orderings for
each column index starting from the leftmost column and ending on the rightmost
column. There may be multiple nodes in the same row and same column. In such
a case, sort these nodes by their values.
Return the vertical order traversal of the binary tree.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
"""





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def verticalOrder(self, root, h_dist, v_dist, values):
            if not root:
                return
            
            if h_dist in values:
                values[h_dist].append((v_dist, root.val))
            else:
                values[h_dist] = [(v_dist, root.val)]
                
            self.verticalOrder(root.left, h_dist - 1, v_dist + 1, values)
            self.verticalOrder(root.right, h_dist + 1, v_dist + 1, values)
            
    def verticalTraversal(self, root):
        v_dist = 0
        h_dist = 0
        values = {}  
        result = []
        
        self.verticalOrder(root, h_dist, v_dist, values)
        
        for x in sorted(values.keys()):
            column = [i[1] for i in sorted(values[x])]
            result.append(column)

        return result   








