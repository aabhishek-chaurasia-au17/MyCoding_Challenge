"""
Q - 3 ) Valid Anagram (5 Marks):
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false



def check(str1, str2):
	
	if(sorted(str1)== sorted(str2)):
		print(True)
	else:
		print(False)		

if __name__ == "__main__":

    str1 ="anagram"
    str2 ="nagaram"
    check(str1, str2)

