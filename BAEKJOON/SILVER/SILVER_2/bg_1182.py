from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in range(1, n+1):
    count += len(list(filter(lambda x: sum(x) == m, list(combinations(arr, i)))))
print(count)
