n, m = map(int, input().split())
arr = list(sorted(set(map(int, input().split()))))
stack = [0]

def permutation(n, m):
    if len(stack) == m+1:
        print(*stack[1:])
        return
    
    for x in arr:
        if stack[-1] <= x:
            stack.append(x)
            permutation(n, m)
            stack.pop()

permutation(n,m)