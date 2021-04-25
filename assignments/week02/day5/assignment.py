# Q. What are the default data types in python?
"""
ans. This is Python's default data type.
     There are 4 basic datatypes:
1. Integers : int.
2. Floating-Point Numbers : float.
3. Boolean Type : bool.
4. Strings : str"".
"""

# Q.  What is typecasting in python?
"""
ans. Type Casting is the method to convert the variable data type into a certain data type in order to 
the operation required to be performed by users.
"""

# Give two examples each of typecasting between each of the following types:
# a. string to boolean
#ex 1
a = "abhishek"
a = bool(a)
print(a, type(a))

# ex 2
b = "chaurasia"
b = bool(b)
print(b, type(b))


# b. integer to boolean
# ex 1
c = 10
c = bool(c)
print(c, type(c))

# ex 2
d = 786
d = bool(d)
print(d, type(d))


# c. boolean to string
# ex 1
e = True
e = str(e)
print(e, type(e))

# ex 2
f = False
f = str(f)
print(f, type(f))


# d. string to integer
# ex 1
x = "12345"
x = int(x)
print(x, type(x))

# ex 2
y = "783808"
y = int(y)
print(y, type(y))
