
"""
Q-3 ) Middle of the Linked List (5 marks)
https://leetcode.com/problems/middle-of-the-linked-list/
(Medium)
Given a non-empty, singly linked list with head node head, return a middle node
of linked list.
If there are two middle nodes, return the second middle node.
Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3. (The judge's serialization of this node is
[3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next
= NULL.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
            slow = head.next
            fast = head.next

            if not head or head.next is None:
                return head

            while slow is not None and fast.next is not None and fast.next.next is not None:

                slow = slow.next
                fast = fast.next.next

            return slow


    if __name__ == "__main__":

            head = [1,2,3,4,5]
        