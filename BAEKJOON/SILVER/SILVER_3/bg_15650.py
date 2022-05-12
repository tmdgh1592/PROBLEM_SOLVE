n, m = map(int, input().split())
result = [0]


def dfs(n, m):

    if len(result) == m+1:
        print(*result[1:])
        return

    for i in range(1, n+1):
        if i not in result and i > result[-1]:
            result.append(i)
            dfs(n, m)
            result.pop()


dfs(n, m)
