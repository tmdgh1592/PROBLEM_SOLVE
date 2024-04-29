def solution(prices):
    s = []
    answer = [0] * len(prices)

    for i, price in enumerate(prices):
        while s and price < prices[s[-1]]:
            j = s.pop()
            answer[j] = i - j
        s.append(i)

    for i in s:
        answer[i] = len(prices) - i - 1

    return answer