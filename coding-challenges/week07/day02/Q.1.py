
"""
Given a sorted Integer array , Write a Program to search the target
element using Binary Search, If target element is found return the index .
Otherwise return -1 .
Input : arr = [1,2,3,15,16,19,23,55,1000] , target = 15
Output: - 3
Explanation:
Just Use Binary search method
Sample :
def Binarysearch(arr , target):
"""

#write code here

def Binarysearch (arr, l, h, target):
    if l > h:
        return -1
     
    mid = (l + h) // 2
    if arr[mid] == target:
        return mid
 
    if arr[l] <= arr[mid]:
 
        if target >= arr[l] and target <= arr[mid]:
            return Binarysearch(arr, l, mid-1, target)
        return Binarysearch(arr, mid + 1, h, target)
 
    if target >= arr[mid] and target <= arr[h]:
        return Binarysearch(mid + 1, h, target)
    return Binarysearch(arr, l, mid-1, target)
 
arr = [1,2,3,15,16,19,23,55,1000]
target = 15
i = Binarysearch(arr, 0, len(arr)-1, target)
if i != -1:
    print ("Index: % d"% i)
else:
    print ("target not found")

 
# Time Complexity: O(log n). 
# Space Complexity: O(1). 
