# 15, 2 | 5
# 2 11 14 17 21

def f(rocks, distance, n, mid):
    removed = 0
    cur = 0
    for rock in rocks:
        if rock - cur < mid:
            removed += 1
        else:
            cur = rock

    removed += int(distance - cur < mid)
    return removed <= n


def solution(distance, rocks, n):
    lo, hi = 1, 1_000_000_000
    rocks.sort()

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if f(rocks, distance, n, mid):
            lo = mid
        else:
            hi = mid

    return lo
