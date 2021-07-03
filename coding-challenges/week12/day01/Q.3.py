
"""
Q-3 ) Kth Smallest Element in a BST (5 marks)
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
(Medium)
Given the root of a binary search tree, and an integer k, return the kth
(1-indexed) smallest element in the tree.
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1
Marks distribution:
Question 1,2 and 3 carry 5 marks each
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k):
        
        stack = []
        count  = 0
        ans = -1
        while(count != k):
            while(root):
                stack.append(root)
                root = root.left            
            root = stack.pop()
            ans = root.val
            count += 1
            root = root.right
        return ans
