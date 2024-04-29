def solution(n, number):
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        dp[i].add(int(str(n) * i))
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    if x + y > 0: dp[i].add(x + y)
                    if x - y > 0: dp[i].add(x - y)
                    if x * y > 0: dp[i].add(x * y)
                    if x // y > 0: dp[i].add(x // y)
        if number in dp[i]:
            return i
    return -1
