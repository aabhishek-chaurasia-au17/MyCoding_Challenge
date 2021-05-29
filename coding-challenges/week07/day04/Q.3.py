"""
Given an array with NO Duplicates . Write a program to find PEAK
ELEMENT
Return value corresponding to the element of the peak element.
Example :
Input : - arr = [2,5,3,7,9,13,8]
Output : - 5 or 13 (anyone)
HINT : - Peak element is the element which is greater than both
neighhbours.
def FindPeak(arr ):
"""
# write code here

def FindPeak(arr):
    l=len(arr)
    
    if(arr[0]>arr[1]):
        
        print(arr[0])

    if(arr[l-1]>arr[l-2]):
      
        print(arr[l-1])
    
    for i in range(1,l-1):
        
        if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
            print(arr[i])
        

arr = [10,2,5,3,7,9,13,81]
FindPeak(arr)