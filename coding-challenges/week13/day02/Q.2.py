"""
Q-2 )Solve above question with DP (5 marks)
"""


class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [1,1]
        if n>=2:
            for i in range(2,n+1):
                steps.append(steps[i-1] + steps[i-2])

        return steps[-1]


if __name__ =="__main__":
    ans = Solution

