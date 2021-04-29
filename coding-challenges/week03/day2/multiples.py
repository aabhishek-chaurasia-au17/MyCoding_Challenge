# a. Given a number as input from the user, print all its odd multiples from 1 to 21 if the number is odd
# and all even multiples from 2 to 20 if the number is even. Use both for loop and while loop.

# this question is by using for loop 
user_input = int(input("Please enter a no. : "))

if user_input % 2 == 0:
    print("Multiple of ", user_input)
    for i in range(2,21,2):
        print(user_input , "X", i, "=", user_input*i )
elif user_input % 2 == 1:
    print("Multiple of ", user_input)
    for i in range(1,22,2):
        print(user_input , "X", i, "=", user_input*i )


# by using while loop 

user_input = int(input("Please enter a no. : "))

if user_input % 2 == 0:
    a = 2
    print("Multiple of ", user_input ,)
    while a <= 20:
        print(user_input ,  "X", a, "=", user_input*a )
        a += 2
elif user_input % 2 ==1 :
    a = 1
    print("Multiple of ", user_input )
    while a <= 21:
        a += 2
        print(user_input ,  "X", a, "=", user_input*a )
   

