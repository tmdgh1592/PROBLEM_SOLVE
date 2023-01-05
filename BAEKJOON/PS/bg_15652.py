n, m = map(int, input().split())
result = [0]


def dfs(n, m):

    if len(result) == m+1:
        print(*result[1:])
        return

    for i in range(1, n+1):
        if i >= result[-1]:
            result.append(i)
            dfs(n, m)  # 반복 (사실상 2중 for문 같은 기능)
            result.pop()


dfs(n, m)
