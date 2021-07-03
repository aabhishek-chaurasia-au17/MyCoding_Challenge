"""
Q-3 ) Binary Tree Tilt (5 marks)
https://leetcode.com/problems/binary-tree-tilt/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self._tilt = 0
        self.dfs(root)
        return self._tilt
        
    def dfs(self, node):
        if node is None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self._tilt += abs(left-right)
        return left+right+node.val