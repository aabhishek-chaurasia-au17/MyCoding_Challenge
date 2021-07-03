"""
Q-3) N-ary Tree Preorder Traversal (5 marks)
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
Given the root of an n-ary tree, return the preorder traversal of its nodes'
values.
pay attention, n is not defined. Write a code that can traverse a tree for any
value of “n” in “n-ary”.
Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
explanation:
Input is top to bottom, left to right fashion.
first element root, will be followed by null.
3,2,4 are children of 1, followed by null means, children of 1 are over.
then 5,6 are children of 3.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        tree = [root.val]
        if root.children:
            for child in root.children:
                tree += self.preorder(child)
        return tree


    
