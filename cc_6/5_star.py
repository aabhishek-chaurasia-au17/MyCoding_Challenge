# a. Print the following pattern after taking in the line number as input from the user:
# for example: if input line number is 5, then print the following pattern.
#   *
#  ***
# *****
#  ***
#   * 

n = int(input("Enter the number of lines you want: "))

for i in range(1, n//2 + n % 2 + 1):
    print(" "*(n-i), "*"*(2*i-1), " "*(n-i))

for i in range(n//2 + n % 2-1, 0, -1):
    print(" "*(n-i), "*"*(2*i-1), " "*(n-i))