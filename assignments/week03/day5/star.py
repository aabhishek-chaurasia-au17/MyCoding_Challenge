# Assignment Week 3
# [All questions need to be solved using both for and while loop]

# 1. Write code for the following sequence by taking line number as user input: 
n = int(input("Please enter Odd number of line. : "))

# By using for loop
def by_for_loop():
    print("By using for loop")
    a = -1
    for i in range(1,n+1):
        if i <=((n//2)+1):
            a += 1
            print(a*" ",1 * "**")
        elif i >((n//2)+1):
            a -= 1
            print(a*" ",1 * "**")



# by using while loop
def by_while_loop():
    print("By using while loop")
    a = -1
    while a < (n//2):
        a += 1
        print(a*" ",1 * "**")
    while a > 0:
        a -= 1
        print(a*" ",1 * "**")

by_while_loop()
by_for_loop()

# 2. Write code for the following sequence by taking line number as user input. 
n = input("Enter in the maximum number of lines: ")
n = int(n)
for ln in range(1, n+1):
  for digit in range(1, ln+1):
    print(ln+1-digit, end="")
  print()


#Using for-loop

n = int(input("Enter the number of lines : "))
for ln in range(1, n+1):
    print(" " * (n - ln),end="")
    for digit in range(1,ln+1):
        print(digit,end="")
        if ln==digit:
            for rev_digit in range(ln-1,0,-1):
                print(rev_digit,end="")
    print()

#Using while-loop

# 3. Write code for the following sequence by taking line number as user input 

n = int(input("Enter the number of lines : "))

ln=1
while (ln<=n):

    print(" " * (n - ln),end="")

    digit=1
    while digit<=ln:
        print(digit,end="")
        if ln==digit:

            rev_digit=ln-1
            while rev_digit>=1:
                print(rev_digit,end="")
                rev_digit=rev_digit-1

        digit=digit+1

    print()
    ln=ln+1

n = int(input("Enter the number of lines (only odd numbers):  "))

halfway_point = ( n//2 + n%2 )

for ln in range(1,halfway_point+1 ):     
        print(" "*(halfway_point-ln),end="")       
        for digit in range(1, ln + 1):
            print(digit,end="")        
        for rev_digit in range(ln-1,0,-1):
            print(rev_digit,end="")
        print()

for ln in range(halfway_point-1, 0,-1): 
    print(" " * (halfway_point-ln),end="")
    for digit in range(1,ln+1):
        print(digit,end="")
    for rev_digit in range(digit-1,0,-1):
        print(rev_digit,end="")
    print()    



#4. Write code for the following sequence by taking line number as user input, [using a single loop only] 
"""
n = 5
1 
21 
321 
21 
1
"""
# with for loop
n=int(input("Enter number the Number"))
for line in range(1,n//2+n%2+1):
    for rows in range(line,0,-1):
        print(rows,end="")
    print()
    

for line1 in range(n//2,0,-1):
    for rows in range(line1,0,-1):
        print(rows,end="")
    print()
        
# with while loop
n=int(input("Enter number the Number"))
line=1
while line<(n//2+n%2+1):
    rows=line
    while rows>0:
        print(rows,end="")
        rows=rows-1
    line=line+1
    print()

line1=(n//2)
while line1>0:
    rows=line1
    while rows>0:
        print(rows,end="")
        rows=rows-1
    line1=line1-1
    print()


#5. Write a function that takes line number as input (with default value of 5) and prints the following pattern.
"""
n=3
.....
.. ..
. .
.. ..
.....
n = 5
.......
... ...
.. ..
. .
.. ..
... ...
....... 

"""
# by using for loop 

ln = 1
n = int(input("Enter the line number: "))
for ln in range(1, n+1):
    print("."*(n-ln),end="")
    print(" "*(2*ln-1),end="")
    print("."*(n-ln))
    
for ln in range(n-1, 0, -1):
    print("."*(n-ln),end="")
    print(" "*(2*ln-1), end="")
    print("."*(n-ln))




n = int(input("Enter the line number: "))
a = n-1
for i in range(1,2*n):
    while i <= n:
        print("."*(n-i),end="")
        print(" "*(2*i-1),end="")
        print("."*(n-i))
        break
    while i > n:
        print("."*(i-n),end="")
        print(" "*(2*a-1), end="")
        print("."*(i-n))
        a-=1
        break

