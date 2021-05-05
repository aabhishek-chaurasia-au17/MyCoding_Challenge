# Write a function called MaxSeq() which can take any number of inputs from the
# user and returns the highest number in that sequence as the output.
# [You cannot use the inbuilt function max() of python]
# Ex:
# Input 1:
# 11 2 3 4
# Output 1:
# 11
# Input 2:
# 1 2 3 8 7
# Output 2:
# 8

def list_pro():
    a = input("Enter the list as space separated numbers: ")
    lis = a.split(" ")
    print("List that we have", lis)
    b = []
    for i in lis:
        b.append(int(i))
    print("Converted list we have",b)
    c = 0
    for i in b:
        if i > c:
            c = i
    print("The higest number in the list is : ", c)   

list_pro()