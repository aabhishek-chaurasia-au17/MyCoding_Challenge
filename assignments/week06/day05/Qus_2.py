"""
Questions:2
Given a integer array , find all the numbers which are palindrome:
Note : -Palindromes are numbers when reversed will get the same as the
original number.
121 - >palindrome , 123 → not a palindrome
Input: [1 , 2 , 256 , 252 , 1441 , 969 ,2331]
Output: [1 , 2 , 252 , 1441 , 969 ]
"""

#Time Complexity = O()
#Space complexity= O()

def palindromeNumbers(list_a): 
  
    c = 0
    for i in list_a:             
        t = i 
        rev = 0
        while t > 0: 
            rev = rev * 10 + t % 10
            t = t // 10
        if rev == i: 
            print (i) 
            c = c + 1
  
    print() 
list_a =[1 , 2 , 256 , 252 , 1441 , 969 ,2331]
palindromeNumbers(list_a) 