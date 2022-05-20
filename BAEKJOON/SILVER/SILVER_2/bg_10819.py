from itertools import permutations

n = int(input())
arr_list = list(permutations(list(map(int, input().split())), n))
max_sum = 0

for arr in arr_list:
    temp_sum = 0
    for i in range(n-1):
        temp_sum += abs(arr[i] - arr[i+1])
    max_sum = max(max_sum, temp_sum)

print(max_sum)
