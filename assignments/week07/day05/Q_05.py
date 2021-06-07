'''
Q5.
https://leetcode.com/problems/majority-element/ .
'''
class Solution(object):
	def majorityElement(self, nums):
		if nums==[]:
			return 0
		n=set(nums)
		maxm = 0
		for x in n:
			t = nums.count(x)
			if t > maxm:
				maxm=t
				m=x
		return m