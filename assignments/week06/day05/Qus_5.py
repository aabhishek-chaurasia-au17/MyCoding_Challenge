"""
Question 5 :
----------------
Given an array arr[], find the maximum j – i such that arr[j] > arr[i] .
Input :- arr = [ 34, 8, 10, 3, 2, 80, 30, 33, 1]
Output : - 6 (j = 7, i = 1)
Explanation : -
Since at index ( j = 6 and i = 1 ) , we get maximum ( j - i ) where arr[j] > arr[i]
Sample :
Def find_max ( arr ):
Note : -
Find Time and Space Complexity of each Question given - (1 - 5 )
"""

#Time Complexity=O(n^2)

#Space complexity= O()


def maxIndexDiff(arr, n):
    maxDiff = -1
    for i in range(0, n):
        j = n - 1
        while(j > i):
            if arr[j] > arr[i] and maxDiff < (j - i):
                maxDiff = j - i
            j =j-1
 
    return maxDiff

arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
n = len(arr)
maxDiff = maxIndexDiff(arr, n)
print(maxDiff)