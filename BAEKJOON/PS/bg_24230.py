import sys
input = sys.stdin.readline

n = int(input())
color_list = [0]+list(map(int, input().split()))
count = 0 if color_list[1] == 0 else 1

for i in range(n-1):
    p, c = sorted(map(int, input().split()))
    if color_list[p] != color_list[c]:
        count += 1

print(count)
