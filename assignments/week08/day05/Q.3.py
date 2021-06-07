"""
Q - 3 ) Find largest number in a list, and second largest number, (without
using inbuilt functions).
eg:
A = [1,3,4,5,8,1,2,3,4,9,6,9]
return 9 and 8.
Write time and space complexity of your code.
(3 marks)
"""




def findLargestNum(arr):
    bigNum = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > bigNum:
            bigNum = arr[i]

    return bigNum


def findLargIndex(arr):
    bigNum = arr[0]
    largeNumidx = 0
    for i in range(0, len(arr)):
        if arr[i] > bigNum:
            bigNum = arr[i]
            largeNumidx = i

    return largeNumidx


def secondLargNum(arr, index):
    secondbigNum = arr[0]
    for i in range(0, len(arr)):
        arr[index] = 0
        if arr[i] > secondbigNum:
            secondbigNum = arr[i]
           
    return secondbigNum




if __name__=="__main__":

    arr = [15, 3, 4, 5, 8, 11, 2, 10, 4, 9, 6, 19]

    result = findLargestNum(arr)
    print("largest number in a list:", result)

    index = findLargIndex(arr)

    result = secondLargNum(arr, index)
    print("second largest number in a list:", result)

