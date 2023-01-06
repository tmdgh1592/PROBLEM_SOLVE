import heapq

x = int(input())
sticks = [64]

while sum(sticks) > x:
    min_stick = heapq.heappop(sticks)
    a, b = min_stick // 2, min_stick - min_stick // 2
    if a + sum(sticks) >= x:
        heapq.heappush(sticks, b)
    elif b + sum(sticks) >= x:
        heapq.heappush(sticks, a)
    else:
        heapq.heappush(sticks, a)
        heapq.heappush(sticks, b)

print(len(sticks))