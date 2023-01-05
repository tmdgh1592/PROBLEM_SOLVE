import sys
input = sys.stdin.readline

n = int(input())
car_in = {}
car_out = []
count = 0

for i in range(n):
    car_in[input()] = i

for _ in range(n):
    car_out.append(input())

for i in range(n-1):
    for j in range(i+1, n):
        first_out = car_out[i]
        last_out = car_out[j]
        # 만약 먼저 나간 차의 입장 순서가 더 크다면 추월
        if car_in[first_out] > car_in[last_out]:
            count += 1
            break

print(count)
