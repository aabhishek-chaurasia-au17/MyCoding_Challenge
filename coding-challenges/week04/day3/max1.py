# Write a function which takes a list as an input from the user [using the input()
# command] and returns the highest and the second highest elements of a list.
# Ex:
# Input 1:
# 1 2 3 4
# Output 1:
# 3 4
# Input 2:
# 1 2 3 8 7
# Output 2:
# 7 8

def list_pro():
    a = input("Enter the list as space separated numbers: ")
    lis = a.split(" ")
    print("List that we have", lis)
    b = []
    for i in lis:
        b.append(int(i))
    print("Converted list we have", b)
    first_largest_int = max(b)
    b.remove(first_largest_int)
    second_largest_int = max(b)
    print("First Highest : ", first_largest_int)
    print("Second Highest : ", second_largest_int)

list_pro()
