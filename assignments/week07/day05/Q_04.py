'''
Write a program to compute the power of a number.
Input - x = 10 , y = 5 , calculate = (x^y)
Output : - 100000
Example -
pow(n, 5) will give you n to the power 5. Use recursion in it.
 '''
def power(x, y):
 
    if (y == 0): return 1
    elif (int(y % 2) == 0):
        return (power(x, int(y / 2)) *
               power(x, int(y / 2)))
    else:
        return (x * power(x, int(y / 2)) *
                   power(x, int(y / 2)))
 
# Driver Code
x = 2; y = 3
print(power(x, y))