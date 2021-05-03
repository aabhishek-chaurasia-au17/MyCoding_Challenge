# Take 2 sequences of space separated integers as input from the user and convert
# it into a list of integers. Extend the first list with all the items of the
# second list and print the output.
# Ex:
# Input 1:
# 1 2 3 4
# 11 434 1
# Output 1:
# 1 2 3 4 11 434 1
# Input 2:
# 1 2 3
# 8 7
# Output 2:
# 1 2 3 8 7
# Hint: Consider using the inbuilt extend() function of lists in python


my_list = []
    
my_list2 = []
    
n = int(input("enter the size of list : "))
   

for i in range(0,n):
    a = int(input("Add Number in List 1 : "))
    my_list.append(a)
print("List 1" , my_list)

d = int(input("enter the size of list 2: "))
for j in range(0,d):
    b = int(input("Add Number in List 2 : "))
    my_list2.append(b)
print("List 2" , my_list2)

my_list.extend(my_list2)
    
print("Extend List is", my_list )