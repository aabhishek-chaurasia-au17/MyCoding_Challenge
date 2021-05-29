"""
Given a sorted array with Duplicates . Write a program to find LOWER
BOUND of a TARGET using Binary search Method .
Return Index corresponding the element of lower bound element.
Example :
Input : - arr = [1,1,1,2,2,3,3,5,5,5,7,7] , Target = 4
Output : - 6
def Lower_Bound(arr , target):
"""    
# write code here 

arr = [1,1,1,2,2,3,3,5,5,5,7,7]
target = 4

def Lower_Bound(arr,target):
    prev = -1 
    for i in range (0,len(arr)):
        if (target==arr[i]):
            return i 
        elif arr[i] > target:
            return prev
        prev = i 

print(Lower_Bound(arr,target))