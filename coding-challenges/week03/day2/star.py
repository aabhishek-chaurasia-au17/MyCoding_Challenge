# b. Given a number as input from the user, print a triangle like the following.

# give codes containing for loop and while loop

user_input=int(input("Enter any number: "))

# by using While loop


i=1
while i <= user_input:
    print("*"*i)
    i=i+1
i=user_input
while i >= 0:
    print("*"*i)
    i=i-1

# by using for loop

for i in range(0, user_input):
  print("*"*i)    
  

for i in range(user_input, 0 , -1):
  print("*"*i)