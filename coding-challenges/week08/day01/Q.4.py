"""
Q-4 ) [Bonus Question] Recursive implementation of binary search:
(5 extra marks)
We have seen an iterative approach for binary search algorithm , write a
recursive approach for that.
HINT: when we divide the array into two parts, we need to perform a search on only one half.
Apply binary search only on that half.
"""

def binarySearch (arr, l, r, x):

	if r >= l:

		mid = l + (r - l) // 2

		if arr[mid] == x:
			return mid
		
		elif arr[mid] > x:
			return binarySearch(arr, l, mid-1, x)

		else:
			return binarySearch(arr, mid + 1, r, x)

	else:
			return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
	print ("Element is present at index % d" % result)
else:
	print ("Element is not present in array")
