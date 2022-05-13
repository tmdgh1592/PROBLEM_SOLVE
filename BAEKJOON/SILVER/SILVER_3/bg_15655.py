n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = [0]

def permutation(n, m):
    if len(result) == m+1:
        print(*result[1:])
        return

    for x in arr:
        if x not in result and x > result[-1]:
            result.append(x)
            permutation(n, m)
            result.pop()

permutation(n, m)