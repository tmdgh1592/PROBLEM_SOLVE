import sys
sys.setrecursionlimit(int(1e6))


def solution(alp, cop, problems):
    max_alp = max(problem[0] for problem in problems)
    max_cop = max(problem[1] for problem in problems)
    problems.extend([[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]])
    memo = [[-1] * 151 for _ in range(151)]

    def dp(apower, cpower):
        if apower == max_alp and cpower == max_cop:
            return 0
        if memo[apower][cpower] != -1:
            return memo[apower][cpower]

        min_time = int(1e9)
        for problem in problems:
            if apower >= problem[0] and cpower >= problem[1]:
                next_alp = min(max_alp, apower + problem[2])
                next_cop = min(max_cop, cpower + problem[3])
                if (next_alp, next_cop) == (apower, cpower): continue
                min_time = min(min_time, dp(next_alp, next_cop) + problem[4])

        memo[apower][cpower] = min_time
        return min_time

    return dp(alp, cop)