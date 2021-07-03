
"""
Q-2 )Remove Duplicates from Sorted List (5 marks)
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
(Easy)
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.
Example 1:
Input: head = [1,1,2]
Output: [1,2]
Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    def deleteDuplicates(self, head):

        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        cur = head
        while cur!=None and cur.next!=None:

            if cur.val==cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head


if __name__ == "__main__" :

    head = [1,1,2,3,3]
    # Solution(head)    


