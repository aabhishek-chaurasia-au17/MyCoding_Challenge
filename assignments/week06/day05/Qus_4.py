"""
Questions : 4 -
--------------------
Given an array of size n and a number k, find all elements that appear
more than n/k times
Input : k = 4 ,n=9 , A = [ 3 ,1, 2, 2, 2, 1, 4, 3, 3 ]
Output: - [ 3 , 2]
Explanation : - val = n/k = (9/4) = 2 (integer part)
Now , take count of each element , we get
Count of element 3 -> 3
Count of element 1 -> 2
Count of element 2 -> 3
Count of element 4 -> 1
Since 3 and 2 are only elements which are having count greater than 2 .
"""

#Time Complexity=O(n)

#Space complexity=O(K)

def N_By_K_Times(arr, n, k) :
    x = n // k
    freq = {}
    for i in range(n) :    
        if arr[i] in freq :
            freq[arr[i]] += 1
        else :
            freq[arr[i]] = 1
    for i in freq :
         if (freq[i] > x) :
            print(i)
          
arr = [3 ,1, 2, 2, 2, 1, 4, 3, 3 ]
n = len(arr)
k = 4
N_By_K_Times(arr, n, k)
