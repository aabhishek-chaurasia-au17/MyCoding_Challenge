"""
Question 3. Write a program to find the length of a string using
recursion.
"""
def string_length(my_string):
  count = 0
  
  for letter in my_string:
    print(letter)
    count = count +1
    
  return count

print(string_length("AttainU"))