
"""
Q - 1 ) Write a program to find the upper bound (first occurrence’s index) of
a target given by the user, that should be present in the list. Using linear
search.
eg:
A= [1,1,1,2,2,2,3,3,4]
lower bound of 2 = 3
upper bound of 2 = 5
Your code should return 5.
Write time and space complexity of your code.
(3 marks)
"""


def upperbound(A, target):
    n = len(A)
    prev = -1
    for i in range(n - 1, -1, -1):
        if target == A[i]:
            return i
        elif target > A[i]:
            return prev
        prev = i


if __name__ == "__main__":

    A = [1,1,1,2,2,2,3,3,4]
    x = 2
    print("upper bound :", upperbound(A, x))

