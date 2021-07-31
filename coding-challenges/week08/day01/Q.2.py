"""
Q-2 ) Write a function that prints digits of a number from left to right , using
recursion:(5 marks)
Sample Input:
1234567
Sample output:
1
2
3
4
5
6
7
"""

def get_digit(num):
    if num < 10:
        print(num)
    else:
        get_digit(num // 10)
        print(num % 10)

get_digit(1234567)