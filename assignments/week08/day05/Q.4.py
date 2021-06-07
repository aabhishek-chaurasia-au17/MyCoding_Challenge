"""
Q - 4 ) Check If N and Its Double Exist:
https://leetcode.com/problems/check-if-n-and-its-double-exist/
Given an array arr of integers, check if there exists two integers N and M such
that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two indices i and j such that :
● i != j
● 0 <= i, j < arr.length
● arr[i] == 2 * arr[j]
Example :
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Write time and space complexity of your code.
(3 marks)
"""





def findExists(arr):
    temp = False
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i != j and 0 <= i and j < len(arr):
                if arr[i] / 2 == arr[j]:
                    temp = True
    if temp == True:
        return "true"
    else:
        return "false"



if __name__=="__main__":

    arr = [3,1,7,14]

    result = findExists(arr)
    print(result)



