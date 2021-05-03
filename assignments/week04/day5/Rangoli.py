"""
Alphabet Rangoli - 1
You are given an integer, n. Your task is to print an alphabet rangoli of size .
(Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
#size 3
    ----c----
    --c-b-c--
    c-b-a-b-c
#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
#size 10
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
The center of the rangoli has the first alphabet letter a, and the boundary has
the alphabet letter (in alphabetical order).
[Hint: Use the chr() and ord() function in python and then try to build this
pattern]

"""

n = int(input("Enter the size : "))
letter = 97 + n
width = n * 4 - 3
dashes = width // 2
string = ""

for ln in range(1, n + 1):
    string = string + chr(letter - ln) + "-"
    rev_string = string[::-1]
    rev_string = rev_string[3:]
    line = "-" * dashes + string + rev_string + "-" * dashes
    if ln == 1:
        line = line[:-1]
    dashes = dashes - 2
    print(line)
print()