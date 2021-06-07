
"""
Q - 2 ) Solve question 1 , but use binary search search.
Write time and space complexity of your code.
(3 marks)
"""

def upperbound(A, target):
    n = len(A)
    left = 0
    right = n - 1
    ans = -1
    while left <= right:
        mid = (left + right) >> 1 # or (left + right) // 2
        if A[mid] == target:
            ans = mid
            left = mid + 1
        elif A[mid] > target:
            right = mid - 1
        elif A[mid] < target:
            left = mid + 1

    return ans


if __name__ == "__main__":

    A = [1,1,1,2,2,2,3,3,4]
    x = 2
    print("upper bound :", upperbound(A, x))



