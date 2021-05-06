"""
                               Max of a list - 3
Consider a list (list = []). You can perform the following commands:
1. insert i e: Insert integer e at position i .
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. pop: Pop the last element from the list.
6. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands
where each command will be of the types listed above. Iterate through each
command in order and perform the corresponding operation on your list.
Example:
N = 4
append 1
append 2
insert 1 3
print
append 1: Append to the list, arr=[1].
append 2: Append to the list, arr=[1,2].
insert 1 3: Insert 3 at index 1, arr=[1,3,2].
print: Print the array.
Output:
[1, 3, 2]
Input Format
The first line contains a number n , denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described
above.
Output Format
For each command of type print, print the list on a new line.
Input 1:
11
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
print
pop
reverse
print
Output 1:
[6, 5, 10]
[5, 10, 9, 1]
[9, 10, 5]

"""

final_list = []
def list_insert():
    n = int(input("Please input index number. : "))
    m = int(input("Please input number. : "))
    final_list.insert(n,m)
    print(final_list)


def remove_no():
    a = int(input("Please enter the number that you want to remove : "))
    final_list.remove(a)
    print(final_list)

    
def append_no():
    a = int(input("Please enter the number that you want to insert in the last. : "))
    final_list.append(a)
    print(final_list)

def delete_last_no():
    final_list.pop()
    print(final_list)

def reverse_list():
    final_list.reverse()

append_no()
append_no()
append_no()
append_no()
list_insert()
remove_no()
delete_last_no()
delete_last_no()
reverse_list()

print(final_list)