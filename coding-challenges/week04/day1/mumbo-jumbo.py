# Define a function factorial() with one input n. [The default value of n needs to be 5]. 
# Use the factorial() function and other inbuilt functions to find the maximum between the following:
# 1. 5!+3!-21 and 2!+4!+12
# 2. 26!+31! and 22!+35!
# 3. 21!+34!-15! and 31!+27!-19!

def factorial_1():
    n = int(input("Enter the Number : "))
    fact = 1
    for num in range(1 , n+1):
        fact = fact * num 
    print("Factorial of ", n, " is : ", fact)
    return fact
factorial_1()

def factorial(n):
    # n = int(input("Enter the Number : "))
    fact = 1
    for num in range(1 , n+1):
        fact = fact * num 
    print("Factorial of ", n, " is : ", fact)
    return fact
    
#factorial()    

print("""\nUse the factorial() function and other inbuilt functions to find the
maximum between the following:
1. 5!+3!-21 and 2!+4!+12
2. 26!+31! and 22!+35!
3. 21!+34!-15! and 31!+27!-19!\n""")

# 1. 5!+3!-21 and 2!+4!+12

fact_1 = factorial(5)
fact_2 = factorial(3)
# fact_3 = factorial(26)

a = fact_1 + fact_2 - 21
print(a)

fact_3 = factorial(2)
fact_4 = factorial(4)

b = fact_3 + fact_4 + 12
print(b)

x = max(a,b)
print("Maximum Number is" , x)

# 2. 26!+31! and 22!+35!

fact_5 = factorial(26)
fact_6 = factorial(31)

c = fact_5 + fact_6
print(c)

fact_7 = factorial(22)
fact_8 = factorial(35)

d = fact_7 + fact_8 
print("Maximum Number is", d)

y = max(c,d)
print(y)

# 3. 21!+34!-15! and 31!+27!-19!

fact_9 = factorial(21)
fact_10 = factorial(34)

e = fact_9 + fact_10 -15
print(e)

fact_9 = factorial(31)
fact_10 = factorial(27)

f = fact_9 + fact_10 -19
print(f)

z = max(e,f)
print("Maximum Number is" , z)


