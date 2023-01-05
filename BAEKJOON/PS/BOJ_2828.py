n, m = map(int, input().split())
res = 0
cur = [1, m]

for _ in range(int(input())):
    x = int(input())
    while not(cur[0] <= x <= cur[1]):
        res += 1
        if x > cur[1]:
            cur[0] +=1
            cur[1] +=1
        elif x < cur[0]:
            cur[0] -=1
            cur[1] -=1

print(res)