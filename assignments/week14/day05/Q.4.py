
"""
Q-4) Remove Duplicates from Sorted List (3.75 marks)
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
(Easy)
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.
Example 1:
Input: head = [1,1,2]
Output: [1,2]
"""






class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        current = head
        while current!=None and current.next!=None:
            if current.val==current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


