n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 총 비용
result = 0
# 가장 저렴한 비용
min_cost = cost[0]

for i in range(n-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    result += min_cost * dist[i]

print(result)
