"""
Q-1 ) Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/
(5 marks)
(Medium)
Write a function to delete a node in a singly-linked list. You will not be given
access to the head of the list, instead you will be given access to the node
to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list.
Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list
should become 4 -> 1 -> 9 after calling your function.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def deleteNode(self, node):

        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        delElmt = node.next
        node.next = node.next.next

        del(delElmt)


if __name__ == "__main__" :

    head = [4,5,1,9]
    node = 5
    # Solution(node)    

