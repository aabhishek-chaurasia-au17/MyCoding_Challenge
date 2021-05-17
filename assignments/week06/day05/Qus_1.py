"""
Total Questions : 5 
Question 1 :
----------------
Given a Square Matrix of Dimension NXM , find all Non-Diagonal
Elements which are prime Numbers .
Input : [ [1,2,3] , [4,5,6] , [7,8,9] ]
Output: - 2 , 3 , 7
Explanation:
The Non-diagonal elements are: 2, 3 ,4 ,6 ,7,8
So the prime numbers among them are : - [ 2,3,7 ]
Answer: - 2,3,7.
Sample :
Def func(Matrix):
"""

#Time Complexity=O(n^2)
#Space complexity=

def Check_Prime_number(n):
    if n == 1:
        return False
    is_prime = True
    for div in range(2, n):
        if n % div == 0:
            is_prime = False
            break
    return is_prime

def Non_Diag_Primes(matrix):
    primes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and Check_Prime_number(matrix[i][j]):
                primes.append(matrix[i][j])
    return primes


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("Matrix :", matrix)
print("Non-Diagonal Elements Which are also Primes :", Non_Diag_Primes(matrix))

