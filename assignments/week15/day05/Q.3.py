


"""
Q-3) Dota2 Senate (5 marks)
https://leetcode.com/problems/dota2-senate/
(Easy)
In the world of Dota2, there are two parties: the Radiant and the Dire.
The Dota2 senate consists of senators coming from two parties. Now the Senate
wants to decide on a change in the Dota2 game. The voting for this change is a
round-based procedure. In each round, each senator can exercise one of the two
rights:
● Ban one senator's right: A senator can make another senator lose all his
rights in this and all the following rounds.
● Announce the victory: If this senator found the senators who still have
rights to vote are all from the same party, he can announce the victory and
decide on the change in the game.
Given a string senate representing each senator's party belonging. The character
'R' and 'D' represent the Radiant party and the Dire party. Then if there are n
senators, the size of the given string will be n.
The round-based procedure starts from the first senator to the last senator in the
given order. This procedure will last until the end of voting. All the senators who
have lost their rights will be skipped during the procedure.
Suppose every senator is smart enough and will play the best strategy for his
own party. Predict which party will finally announce the victory and change the
Dota2 game. The output should be "Radiant" or "Dire".
Example 1:
Input: senate = "RD"
Output: "Radiant"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right
in round 1.
And the second senator can't exercise any rights anymore since his right has
been banned.
And in round 2, the first senator can just announce the victory since he is the only
guy in the senate who can vote.
"""

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        s, banned = set(), [False] * n
        ban_d = ban_r = 0
        while len(s) != 1:
            s = set()
            for i, p in enumerate(senate):
                if banned[i]: continue
                if p == 'R':
                    if ban_r > 0:        
                        ban_r -= 1
                        banned[i] = True
                    else:                
                        ban_d += 1
                        s.add('R')
                else:        
                    if ban_d > 0:        
                        ban_d -= 1
                        banned[i] = True
                    else:                  
                        ban_r += 1
                        s.add('D')
        return 'Radiant' if s.pop() == 'R' else 'Dire'


