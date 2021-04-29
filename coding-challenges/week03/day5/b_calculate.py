# Redefine the same function with default values for numbers as 3 and 5 and opname as "Add". Use the same 
# function to calculate 5+3-12+23

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
    
    print("**** This is B Question ****")
    print("""For Example "5+3-12+23" """)
    a = 3+5
    b = -12+23
    c = print(a+b)
    return c

# NOTE : for using these function just remove the comment tag(#)

    # add()
    # sub()
    # multiply()
    # divide()
arithmetic_operation()
