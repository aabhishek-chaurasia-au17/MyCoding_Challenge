"""
Question 1 :
---------------
Write a Program to swap values , without using 3rd variable .
Also find Time and Space Complexity 
Example : -
Input : -
A = 20 , B = 10
Output : - A = 10 , B = 20
Explanation : - values has been swapped
Sample :
Def swap(A,B):

"""

#write code here

def swap(a,b):
    
    print(f"Without swaping the value of a is {a} and b is {b} ")    
    a , b = b , a

    print(f"After swaping the value of a is {a} and b is {b} ")    
    # return a, b

swap(10,20)

# Also find Time and Space Complexity --- Marks : - 5

# It's time complexity is :- O(1)

# It's space complexity is :-  O(1)
