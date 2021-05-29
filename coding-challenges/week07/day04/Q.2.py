"""
Given a sorted array with Duplicates . Write a program to find UPPER
BOUND of a TARGET using Binary search Method .
Return Index corresponding to the element of the upper bound element.
Example :
Input : - arr = [1,1,1,2,2,3,3,5,5,5,7,7] , Target = 4
Output : - 7
def Upper_Bound(arr , target):
"""

# write code here



def Ub_bs(arr,target):
    
    l=len(arr)
    
    res,left,right=-1,0,l-1
    
    while(left<=right):
    
        mid=(left+right)//2
    
        if(arr[mid]==target):
    
            left=mid+1
    
        elif(arr[mid]>target):
    
            right=mid-1
    
        else:
    
            left=mid+1
    
    return mid


arr=[1,1,1,2,2,2,3,3,5,5,7,7]
    
target=4

print(Ub_bs(arr,target))