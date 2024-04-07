def solution(s):
    s = [s[i] * (1 if i % 2 != 0 else - 1) for i in range(len(s))]
    dp = [[0, 0] for _ in range(len(s))]
    dp[0] = [s[0], s[0]]

    for i in range(1, len(s)):
        num = s[i]
        dp[i][0] = min(dp[i - 1][0] + num, num)
        dp[i][1] = max(dp[i - 1][1] + num, num)

    answer = -float('inf')
    for x, y in dp:
        answer = max(answer, abs(x))
        answer = max(answer, abs(y))
    return answer
