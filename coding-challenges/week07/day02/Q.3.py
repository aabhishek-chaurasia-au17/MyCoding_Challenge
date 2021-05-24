
"""
Given an sorted integer array . Write a program to find UPPER Bound of
target number , return the index of the element .
Input : - [1,2,2,2,3,3,5,5,5,6,6,7,7] , target = 7
Output: - 12
Explanation : HINT - already discussed in class;
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
 
arr = [1,2,2,2,3,3,5,5,5,6,6,6,7,7]
target = 7
i = Binarysearch(arr, 0, len(arr)-1, target)
if i != -1:
    print ("Index: % d"% i)
else:
    print ("target not found")

 
# Time Complexity: O(log n). 

# Space Complexity: O(1). 