import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline


def dfs(arr: list, n):
    global count
    if sum(arr) == n:
        count += 1
        return

    for i in range(1, 4):
        if i + sum(arr) <= n:
            arr.append(i)
            dfs(arr, n)
            arr.pop()
        else:
            return


T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    count = 0
    dfs([], n)
    print(count)
