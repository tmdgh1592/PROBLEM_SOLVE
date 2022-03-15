from bisect import bisect_left

# {10 30 10 20 20 10} =>
# {-10 -30 -10 -20 -20 -10} =>
# {-30 -20 -10} =>
# {30 20 10}

def minus(x):
    return -1 * int(x)

n = int(input())
arr = list(map(minus, input().split()))
dp = [arr[0]]

for i in range(1, n):
    if(dp[-1] < arr[i]):
        dp.append(arr[i])
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))
