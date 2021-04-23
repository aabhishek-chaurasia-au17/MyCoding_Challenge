# Take a number as input from the user, print its multiple of 2, 4, 6, 8, 10 if it is an odd number, 
# if it is an even number then print its multiple of 1, 3, 5, 7 and 9.

num = int(input("Enter the number : "))

if num % 2 == 0:
    print("its even number")
    print(num, "* 2 =", num*2)
    print(num, "* 4 =", num*4)
    print(num, "* 6 =", num*6)
    print(num, "* 8 =", num*8)
    print(num, "* 10 =", num*10)
    
else:
    print("its odd number")
    print(num, "* 1 =", num*1)
    print(num, "* 3 =", num*3)
    print(num, "* 5 =", num*5)
    print(num, "* 7 =", num*7)
    print(num, "* 9 =", num*9)
    