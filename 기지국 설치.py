from math import ceil


def solution(n, stations, w):
    answer = 0
    r = 2 * w + 1
    cur = 1

    for station in stations:
        cnt = station - w - cur
        if station - w > cur:
            answer += ceil(cnt / r)
        cur = station + w + 1

    if cur <= n:
        cnt = n + 1 - cur
        answer += ceil(cnt / r)
    return answer
