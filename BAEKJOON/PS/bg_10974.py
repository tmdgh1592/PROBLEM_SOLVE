from itertools import permutations

arr = [i for i in range(1, int(input()) + 1)]

for i in list(permutations(arr)):
    for j in i:
        print(j, end=' ')
    print()
