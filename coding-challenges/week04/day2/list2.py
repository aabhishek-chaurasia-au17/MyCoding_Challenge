# Accomplish the same task as Lists are US - 1 but without using the built-in
# extend() function of the list data type in python.


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

my_list3 = my_list + my_list2
    
print("Extend List is", my_list3 )