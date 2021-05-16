# Write a program to PRINT numbers from 1 to N , with conditions :
# a) If number is divisible by 7 , print("HI")
# b) If number is divisible by 11 , print("BYE")
# c) If number divisible by both 7 and 11 , print ("HiBYE")
# Also, find the Time complexity for the algorithm.
# Example : -
# N = 12
# Output :
# Hi
# BYE

N = int(input("give a number : "))

for i in range(1,N+1):
    if i % 7 == 0 and i % 11 == 0:
        print("HiBYE")
    
    elif i % 7 == 0:
        print("HI")
    
    elif i % 11 == 0:
        print("BYE")

    
#Time Complexity - O(N)
    