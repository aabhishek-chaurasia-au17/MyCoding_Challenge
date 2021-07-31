'''
Q - 2 ) https://leetcode.com/problems/plus-one/
'''

digits=list(map(int,input("Enter the list = ").split()))
list1=[]
digit_str = [str(x) for x in digits]    #['1','2','3']
joined_str= "".join(digit_str)          #'123'
joined_str=int(joined_str)              #123
joined_str=joined_str + 1               #123+1=124
while joined_str!=0:                    
    last_digit=joined_str%10
    list1.append(last_digit)            #preparing list [4,2,1]
    joined_str=joined_str//10           
list1.reverse()                         #[1,2,4]
print(list1)