n, m = map(int ,input().split())
arr = sorted(list(map(int, input().split())))
result = []

def permutation(n, m):
    if len(result) == m:
        print(*result)
        return
    for x in arr:
        result.append(x)
        permutation(n, m)
        result.pop()

permutation(n, m)