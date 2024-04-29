import sys
sys.setrecursionlimit(int(1e7))


def solution(x, y, n):
    dp = [[-1] * 4 for _ in range(y + 1)]

    def f(number, op):
        if dp[number][op] != -1: return dp[number][op]
        if number > y: return int(1e9)
        if number == y: return 0

        dp[number][op] = int(1e9)
        if number * 3 <= y: dp[number][op] = min(dp[number][op], f(number * 3, 1) + 1)
        if number * 2 <= y: dp[number][op] = min(dp[number][op], f(number * 2, 2) + 1)
        if number + n <= y: dp[number][op] = min(dp[number][op], f(number + n, 3) + 1)

        return dp[number][op]

    ans = f(x, 0)
    return -1 if ans == int(1e9) else ans