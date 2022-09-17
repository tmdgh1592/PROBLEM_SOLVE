import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

N, M = MIS()
arr = list(MIS())

dp = [0] * (N + 1)
cur = 0

if arr[0] > arr[1]:
    dp[1] = arr[0]
else:
    dp[1] = arr[1]
    cur = 1


# i 번 굴렸을 때 눈덩이의 최대 크기
for i in range(2, M+2):
    if cur > N:
        break

    if dp[i-1] + arr[cur+1] > (dp[i-1] // 2) + arr[cur+2]:
        dp[i] = dp[i-1] + arr[cur+1]
        cur += 1
    else:
        dp[i] = (dp[i-1] // 2) + arr[cur+2]
        cur += 2

    print(dp[i])

print(dp[M])