# Fibonacci
# There is a sequence of numbers called the fibonacci numbers where each number
# can be calculated as the sum of the last 2 numbers before it.
# 0,1,1,2,3,5,8,13,....
# In the above sequence you can see that the fourth number 2 is the sum of the
# second and third number 1 and 1. The fifth number 3 is the sum of 2 (fourth
# number) and 1 (third number) and so on.

# Read More Here on this: https://en.wikipedia.org/wiki/Fibonacci_number
# Write a function fibonacci(n) which returns the nth fibonacci number. This
# should be calcuated using the while loop. The default value of n should be 10.

# fibonacci(1)
# >>>0
# fibonacci(2)
# >>>1
# fibonacci(3)
# >>>1
# fibonacci(4)
# >>>2
# fibonacci(5)
# >>>3
# Also find the maximum of:
# fibonacci(12)+fibonacci(10) and fibonacci(11)+fibonacci(11).



def fibonacci(n): 
    if n < 0:
        print("Please input natural number.")
    elif n == 0 :
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
        

def fib():
    a = input("Please write 'yes' for default value fibonacci(10) and 'no' for user input fibonacci(n) : ")
    if a == "yes":
        print("Fibonacci of", 10 ,"is :", fibonacci(10))
    if a == "no":
        n = int(input("Please enter the number : "))
        print("Fibonacci of", n ,"is :", fibonacci(n) )

# to see above code is working or not just uncomment below line  
      
# fib()

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))

# Also find the maximum of:
# fibonacci(12)+fibonacci(10) and fibonacci(11)+fibonacci(11).

a = fibonacci(12)+fibonacci(10)
b = fibonacci(11)+fibonacci(11)

print("fibonacci of (fibonacci(12)+fibonacci(10)) is", a ,"and fibonacci of (fibonacci(11)+fibonacci(11)) is", b )
print("Maximum of fibonacci(12)+fibonacci(10) and fibonacci(11)+fibonacci(11) is", max(a,b))