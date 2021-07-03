"""
Q-3 ) Merge In Between Linked Lists (5 marks)
https://leetcode.com/problems/merge-in-between-linked-lists/
(Medium)
You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their
place.
The blue edges and nodes in the following figure incidate the result:
Build the result list and return its head.
Example 1:
Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [0,1,2,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their
place. The blue edges and nodes in the above figure indicate the result.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeInBetween(self, list1, a, b, list2):

        start = None
        end = list1
        for i in range(b):

            if i == a - 1:
                start = end
            end = end.next
        start.next = list2

        while list2.next:

            list2 = list2.next
        list2.next = end.next
        end.next = None

        return list1


if __name__ == "__main__" :

    list1 = [0,1,2,3,4,5] 
    a = 3
    b = 4
    list2 = [1000000,1000001,1000002]
    # Solution(list1, a, b, list2)    
