"""
Q-2) Find the Town Judge (5 marks)
https://leetcode.com/problems/find-the-town-judge/
(Easy)
In a town, there are n people labelled from 1 to n. There is a rumor that one of
these people is secretly the town judge.
If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person
labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of the town judge.
Otherwise, return -1.
Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
"""



class Solution:
    def findJudge(self, N, trust):
        
        if N == 1:
            return 1
        trust_score = [ 0 for _ in range(N+1) ]
        
        for p1, p2 in trust:
            
            trust_score[p1] -= 1
            
            trust_score[p2] += 1
            
        
        for person in range(1, N+1):
            if trust_score[person] == N-1:
                return person
        
        return -1
