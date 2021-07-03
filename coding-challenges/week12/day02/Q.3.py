"""
Q-3 )Increasing Order Search Tree (5 marks)
https://leetcode.com/problems/increasing-order-search-tree/
(Easy)
Given the root of a binary search tree, rearrange the tree in in-order so that the
leftmost node in the tree is now the root of the tree, and every node has no left
child and only one right child.
Example 1:
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Marks distribution:
Question 1,2 and 3 carry 5 marks each.
"""





class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root):
        stack=[]
        firstNode=True
        
        while True:
            while root:
                stack.append(root)
                root=root.left
                
            if not stack:
                break
            
            node=stack.pop()
            
            if firstNode:
                newRoot=TreeNode(node.val)
                new=newRoot
                firstNode=False
            else:
                newRoot.right=TreeNode(node.val)
                newRoot=newRoot.right
            
            root=node.right
        return new

