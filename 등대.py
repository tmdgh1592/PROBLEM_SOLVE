import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e6))


def solution(n, lighthouse):
    dp = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    mdict = defaultdict(set)
    for x, y in lighthouse:
        mdict[x].add(y)
        mdict[y].add(x)

    def f(node):
        visited[node] = True
        dp[node][1] = 1

        for child in mdict[node]:
            if visited[child]: continue

            f(child)
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child])

    f(1)
    return min(dp[1])