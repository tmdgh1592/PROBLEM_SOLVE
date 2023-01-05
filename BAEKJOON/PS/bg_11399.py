import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

result = 0
total_sum = 0
for x in arr:
    result += x
    total_sum += result

print(total_sum)
