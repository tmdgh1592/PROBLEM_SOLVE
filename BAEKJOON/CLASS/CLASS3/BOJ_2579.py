n = int(input())

arr = [0]+[int(input()) for _ in range(n)]
dp = [0] * (n+1)

if n == 1: print(arr[1])
elif n == 2: print(arr[1] + arr[2])
else: 
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
    dp[3] = max(arr[1] + arr[3], arr[2] + arr[3])

    # 계속 2칸씩 or 2칸 + 1칸 반복
    for i in range(4, n+1):
        dp[i] = max(arr[i] + dp[i-2], arr[i] + arr[i-1] + dp[i-3])

    print(dp[-1])