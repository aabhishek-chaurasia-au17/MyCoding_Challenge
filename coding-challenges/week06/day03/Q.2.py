"""
Question : 2 -
Given a number , find if the number is a perfect square root or not ?
Also , find Time and space Complexity
example :
Input : n = 4
output : - True
Input : n = 10
output : - False
Explanation : since square root (4) =2 (perfect square ) --true
Square root(10) = 3.35 (Not perfect square) -- false
Sample :
Def find_perfect_square(N):
"""

# write code here
# ------------------------------------------------------------

import math

def find_perfect_square():
    
    n = int(input("Enter the Number : "))

    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        print(n, "is a perfect square")
    else:
        print(n, "is not a perfect square")

find_perfect_square()

# Also find Time and Space Complexity --- Marks : - 5

#Time Complexity is: O(N)

#Space Complexity is: O(1)
# ________