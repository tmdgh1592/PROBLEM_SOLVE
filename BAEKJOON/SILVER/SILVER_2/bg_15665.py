n, m = map(int, input().split())
arr = list(sorted(set(map(int, input().split()))))
stack = []
def permutation(n, m):
    if len(stack) == m:
        print(*stack)
        return
    
    for x in arr:
        stack.append(x)
        permutation(n, m)
        stack.pop()

permutation(n,m)