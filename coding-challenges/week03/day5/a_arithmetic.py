# a. Define a function arithmetic_operation() which takes 2 numbers and operation name as 
# input and performs an operation on them:
# * opname: "Add" - Then we add 2 numbers
# * opname: "Sub" - Then we subtract 2 numbers
# * opname: "Multiply" - Then we multiply 2 numbers
# * opname: "Divide" - Then we divide the 2 numbers
# Print the result of the operation and also return it. 

a = int(input("Please enter first number : "))
b = int(input("Please enter second number : "))

def add():
    dialog = print(a+b)
    return dialog

def sub():
    dialog = print(a-b)
    return dialog

def multiply():
    dialog = print(a*b)
    return dialog

def divide():
    dialog = print(a/b)
    return dialog

def arithmetic_operation():
    add()
    sub()
    multiply()
    divide()
arithmetic_operation()
