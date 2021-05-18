"""
Questions : 3 --
Print prime numbers between 1 to N :                        
using for loop :
Also , find the Time and Space complexity
Example : -
Input : - N = 10
output : - [2 , 3 , 5 , 7 ]
Explanation : - 2 , 3 , 5 , 7 are primes number between 1 to 10
Sample :-
Def Prime_number(N):
"""

#write code here


def Prime_number():

    n = int(input("Enter a Number : "))
    list = []

    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            list.append(i)
            
    print(list)
Prime_number()

# Also find Time and Space Complexity --- Marks : - 5

# It's time complexity is :- O(N)

# It's space complexity is :-  O(4)