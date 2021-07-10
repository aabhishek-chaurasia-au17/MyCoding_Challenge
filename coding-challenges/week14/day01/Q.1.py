
"""
Q-1 ) Diameter of a binary tree
https://leetcode.com/problems/diameter-of-binary-tree/description/
(5 marks)
(Easy)
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges
between them.
Example 1:
￼
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ptr = 0
        def recursion(root):
            if not root:
                return 0
            l = recursion(root.left)
            r = recursion(root.right)
            if l+r>self.ptr:
                self.ptr = l+r
            return 1+max(l,r)
        recursion(root)
        return self.ptr

