"""
Q-3 ) Binary Tree Zigzag Level Order Traversal (5 marks)
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
(Medium)
Given the root of a binary tree, return the zigzag level order traversal of its nodes'
values. (i.e., from left to right, then right to left for the next level and alternate
between).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
"""





class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):

        l_to_r = True
        if not root: return
        queue = []
        queue.append(root)
        result = []

        while queue:

            length = len(queue)
            current_res = []
            for _ in range(length):

                if l_to_r:
                    current = queue.pop(0)
                    current_res.append(current.val)
                    if current.left: queue.append(current.left)
                    if current.right: queue.append(current.right)

                else:
                    current = queue.pop()
                    current_res.append(current.val)
                    if current.right: queue.insert(0, current.right)
                    if current.left: queue.insert(0, current.left)
            result.append(current_res)
            l_to_r = not l_to_r

        return result

