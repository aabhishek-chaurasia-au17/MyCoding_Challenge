"""
Q-2 ) Convert Binary Number in a Linked List to Integer: (5 marks)
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
(Easy)
Given head which is a reference node to a singly-linked list. The value of each
node in the linked list is either 0 or 1. The linked list holds the binary
representation of a number.
Return the decimal value of the number in the linked list.
Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def getDecimalValue(head):
    temp = head
    node = 0
    while (temp):
        node += 1
        temp = temp.next
    result = 0
    for i in range(node):
        result += head.val * 2 ** (node - 1 - i)
        head = head.next
    return result


if __name__ == "__main__":

    head = [1,0,1]
    ans = getDecimalValue(head)
    print(ans)

