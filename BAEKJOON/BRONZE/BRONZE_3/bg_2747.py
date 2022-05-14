n = int(input())
dp = [0, 1] + [0] * (n-1)


def F(n):
    if n >= 0 and dp[n] == 0:
        dp[n] = F(n-1) + F(n-2)
    return dp[n]


print(F(n))
