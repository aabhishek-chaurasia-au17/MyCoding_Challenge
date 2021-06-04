# Q-2 ) Program for Sum of the digits of a given number: (5 marks)

    
def sumDigits(no): 
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10))  
    
n = 1234567
print(sumDigits(n))