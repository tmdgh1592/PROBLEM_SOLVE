n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
stack = [0]
result = []
visited = [False] * len(arr)

def permutation(n, m):
    if len(stack) == m+1:
        result.append(tuple(stack[1:].copy()))
        return
    
    for i in range(len(arr)):
        if not visited[i] and arr[i] >= stack[-1]:
            stack.append(arr[i])
            visited[i] = True
            permutation(n, m)
            stack.pop()
            visited[i] = False

permutation(n, m)
result = sorted(set(result))
for r in result:
    print(*r)