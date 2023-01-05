n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []


def dfs(n, m):
    if len(result) == m:
        print(*result)
        return

    for x in arr:
        if x not in result:
            result.append(x)
            dfs(n, m)
            result.pop()


dfs(n, m)
