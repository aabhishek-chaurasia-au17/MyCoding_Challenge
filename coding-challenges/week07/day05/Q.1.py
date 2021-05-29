"""
Question 1. 
Write a program using recursion to countthe number ofvowels in a string.
"""

sentence = input("Enter One Line: ")
string = sentence.lower()
count = 0
list = ["a", "e","i","o","u"]

for i in string:
    if i in list:
        count = count +1

print(f"Vowels are in sentance: {count} ")