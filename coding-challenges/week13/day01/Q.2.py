"""
Q-2 )Solve above question with DP (5 marks)
"""


def fibo(no, dp):
    if no == 0:
        return 0
    
    if no == 1:
        return 1

    if dp[no] is not None:
        return dp[no]
        

    ans = fibo(no - 1, dp) + fibo(no - 2, dp)
    dp[no] = ans
    return ans

if __name__ == "__main__":
    dp = [None] * 10005
    print(fibo(135, dp))


