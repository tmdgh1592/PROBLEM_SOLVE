from itertools import combinations

arr = [int(input()) for _ in range(9)]
for x in list(filter(lambda x: sum(x) == 100, list(combinations(arr, 7))))[0]:
    print(x)
