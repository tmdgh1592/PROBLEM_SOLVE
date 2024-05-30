def solution(stones, k):
    lo = 1
    hi = 200000000

    def f(people):
        jump = 0
        for stone in stones:
            if people >= stone:
                jump += 1
            else:
                jump = 0
            if jump >= k:
                return False
        return True

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if f(mid):
            lo = mid
        else:
            hi = mid

    return hi
