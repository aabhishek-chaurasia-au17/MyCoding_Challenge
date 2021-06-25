"""
Q-2 ) Jewels and StonesJewels and numStones: (5 marks)
https://leetcode.com/problems/jewels-and-stones/
You're given strings jewels representing the types of stones that are jewels, and
stones representing the stones you have. Each character in stones is a type of
stone you have. You want to know how many of the stones you have are also
jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
"""


def numStonesJewels(jewels, stones):
    numStones = {}
    numJewels = 0

    for i in stones:
        if i not in numStones:
            numStones[i] = 1
        else:
            numStones[i] += 1     

    for j in jewels:
        if j in numStones:
            numJewels += numStones[j]

    return numJewels


if __name__ == "__main__":

    jewels = "aA"
    stones = "aAAbbbb"
    ans = numStonesJewels(jewels, stones)
    print(ans)

