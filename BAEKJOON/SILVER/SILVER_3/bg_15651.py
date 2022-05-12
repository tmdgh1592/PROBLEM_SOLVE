n, m = map(int, input().split())
result = []


def dfs(n, m):

    if len(result) == m:
        print(*result)
        return

    for i in range(1, n+1):
        result.append(i)
        dfs(n, m)  # 위 과정 반복
        result.pop()


dfs(n, m)
