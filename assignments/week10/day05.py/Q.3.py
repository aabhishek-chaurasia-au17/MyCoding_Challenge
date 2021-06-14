"""
Q-3 ) Build an Array With Stack Operations (5 marks)
https://leetcode.com/problems/build-an-array-with-stack-operations/
(Medium)
Given an array target and an integer n. In each iteration, you will read a number
from list = {1,2,3..., n}.
Build the target array using the following operations:
● Push: Read a new element from the beginning list, and push it in the array.
● Pop: delete the last element of the array.
● If the target array is already built, stop reading more elements.
Return the operations to build the target array. You are guaranteed that the
answer is unique.
Example 1:
Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation:
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]
Marks distribution:
Question 1,2 and 3 carry 5 marks each.
"""



def buildArray(target, n):
    
    
    res = []
    if len(target) == 0:
        return []
    
    last = target[-1]
    for i in range(1, last + 1):
        
        if i in target:
            res.append("Push")
        else:
            res.append("Push")
            res.append("Pop")

    return res     


if __name__ == "__main__":

    target = [1,3]
    n = 3
    ans = buildArray(target, n)
    print(ans)
