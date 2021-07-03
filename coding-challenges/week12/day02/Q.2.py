
"""
Q-2 )Sum of Root To Leaf Binary Numbers
(5 marks)
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
(Easy)
You are given the root of a binary tree where each node has a value 0 or 1. Each
root-to-leaf path represents a binary number starting with the most significant bit.
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in
binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the
root to that leaf.
Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits
integer.
Example 1:
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
"""





# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root, sum=0):
        if not root:
            return 0
        sum = sum * 2 + root.val
        if root.left or root.right:
            return self.sumRootToLeaf(root.left, sum) + self.sumRootToLeaf(root.right, sum)
        else:
            return sum

