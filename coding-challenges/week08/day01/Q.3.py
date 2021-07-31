"""
Q-3 ) Reverse a string using recursion:(5 marks)
If we have a string, write a function that prints reverse of that string, using
recursion.
Sample Input:
ABCD
Sample Output:
DCBA
"""

def reverse(string):
    if len(string) == 0:
        return
      
    temp = string[0]
    reverse(string[1:])
    print(temp, end='')
  
string = "ABCD"
print("\nReverse of string ", reverse(string))

  



