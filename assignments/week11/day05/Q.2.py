"""
Q-2 ) Palindrome Linked List (5 marks)
https://leetcode.com/problems/palindrome-linked-list/
(Easy)
5612
448
Add to List
Share
Given the head of a singly linked list, return true if it is a palindrome.
Example 1:
Input: head = [1,2,2,1]
Output: true
Example 2:
Input: head = [1,2]
Output: false
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
	def isPalindrome(self, head):
		temp = []
		while head != None:
			temp.append(head.val)
			head = head.next			
		if temp == temp[::-1]:
			return True
		else:
			return False


if __name__ == "__main__":

    Solution()


