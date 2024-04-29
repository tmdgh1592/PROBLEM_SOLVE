def solution(n, times):
    lo = 1
    hi = 1000000000 * 1000000000
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        people = 0

        for time in times:
            people += mid // time

        if people >= n:
            hi = mid
        else:
            lo = mid

    return mid