from itertools import combinations
while(1): k, *l = list(map(int, input().split())); [print(*x) for x in list(combinations(l, 6))]; print() if k else exit(0)