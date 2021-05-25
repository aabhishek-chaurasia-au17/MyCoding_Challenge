
"""
Given an sorted integer array . Write a program to find Lower Bound of
target number, return the index of the element
Input: arr = [1,2 ,3,3,3,4,4,5,5,7,7,7] , target = 6
Output: 8
Explanation : -
def Lower_Bound(arr , target):
"""

# write code here

arr = [1,2,3,3,3,4,4,5,5,7,7,7]
target = 6

def Lower_Bound(arr,target):
    prev = -1 
    for i in range (0,len(arr)):
        if (target==arr[i]):
            return i 
        elif arr[i] > target:
            return prev
        prev = i 

print(Lower_Bound(arr,target))