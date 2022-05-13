n, m =map(int, input().split())
arr = sorted(list(map(int,input().split())))
stack = []
used = [False] * len(arr)
result = []

def permutation(n, m):
    if len(stack) == m:
        result.append(tuple(stack.copy()))
        return
    
    for i in range(len(arr)):
        if not used[i]:
            stack.append(arr[i])
            used[i] = True
            permutation(n, m)
            used[i] = False
            stack.pop()
            
permutation(n, m)
result = sorted(set(result))
for r in result:
    print(*r)