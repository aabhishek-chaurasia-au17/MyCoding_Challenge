# Q-2 )Sort an array of 0s, 1s and 2s:                                (5 marks)

"""
Given an array A[] consisting 0s, 1s and 2s. The task is to write a function
that sorts the given array. The functions should put all 0s first, then all 1s
and all 2s in last.
"""

# Examples:
# Input: {0, 1, 2, 0, 1, 2}
# Output: {0, 0, 1, 1, 2, 2}
# Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
# Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}


def printArr(arr, n):
	for i in range(n):
		print(arr[i],end=" ")


def sortArr(arr, n):
	cnt0 = 0
	cnt1 = 0
	cnt2 = 0
	
	for i in range(n):
		if arr[i] == 0:
			cnt0+=1
		
		elif arr[i] == 1:
			cnt1+=1
			
		elif arr[i] == 2:
			cnt2+=1
	
	i = 0

	while (cnt0 > 0):
		arr[i] = 0
		i+=1
		cnt0-=1
	
	while (cnt1 > 0):
		arr[i] = 1
		i+=1
		cnt1-=1
	

	while (cnt2 > 0):
		arr[i] = 2
		i+=1
		cnt2-=1
	
	printArr(arr, n)


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n = len(arr)

sortArr(arr, n)



