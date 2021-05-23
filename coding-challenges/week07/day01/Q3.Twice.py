"""
Given an integer array , every element is repeated TWICE , except one
element , Find that element ?
Input : - [1 , 2 , 1, 2 ,4 , 3 ,4 ,3]
Output: - 3
Explanation : HINT : - Use XOR operator ;
"""

def findSingle( ar, n):
     
    res = ar[0]
     
    # Do XOR of all elements and return
    for i in range(1,n):
        res = res ^ ar[i]
     
    return res
 
# Driver code
ar = [2, 3, 5, 4, 5, 3, 4]
# arra = int(input("Enter numbers in array format:"))
print("Element occurring once is", findSingle(ar, len(ar)))


#Time Complexity O(n)

#Space Complexity: O(n)